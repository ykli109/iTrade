# -*- coding: utf-8 -*-

# 添加项目根目录到Python路径
import datetime
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import pandas as pd
import requests
from typing import List, Optional
from utils.log import initLog
from data.base import TABLE_BASE
from data.utils import get_field_type_name
from database.utils import insert_db_from_df
from sqlalchemy.exc import SQLAlchemyError
import time
import functools

# 初始化日志
logger = initLog(log_filename='data_fetch.log')

def retry(max_retries=3, delay=5, exceptions=(SQLAlchemyError,)):
    """
    装饰器，用于在发生指定异常时重试函数。

    参数:
        max_retries (int): 最大重试次数。
        delay (int): 每次重试的延迟时间（秒）。
        exceptions (tuple): 需要触发重试的异常类型。

    返回:
        function: 被装饰的函数。
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retries += 1
                    logger.error(f"函数 {func.__name__} 第 {retries} 次重试因错误: {e}")
                    if retries < max_retries:
                        time.sleep(delay)
                    else:
                        logger.error(f"函数 {func.__name__} 达到最大重试次数，操作失败。")
                        raise
        return wrapper
    return decorator

@retry(max_retries=3, delay=5, exceptions=(SQLAlchemyError,))
def write_to_database(df: pd.DataFrame, table_name: str = 'base', db_name: str = 'default'):
    """
    将DataFrame数据写入指定的数据库表中。

    参数:
        df (pd.DataFrame): 要写入的数据。
        table_name (str): 目标数据库表名。
        db_name (str): 数据库配置名称，默认为 'default'。
    """
    if df.empty:
        logger.info("DataFrame为空，跳过写入数据库。")
        return

    try:
        # 提取 columns 中的 map 字段和对应的 key 值
        map_to_key = {v['map']: k for k, v in TABLE_BASE['columns'].items()}
        df.rename(columns=map_to_key, inplace=True)
        # 根据 TABLE_BASE['columns'] 的键排序
        new_order = list(TABLE_BASE['columns'].keys())
        df = df.reindex(columns=new_order)
        # 将数据写入数据库，使用已有的方法
        insert_db_from_df(data=df, table_name=table_name, db_name='default')  # 调用已有的方法
        logger.info(f"成功将数据写入数据库表 '{table_name}'。")
    except SQLAlchemyError as e:
        logger.error(f"将数据写入数据库时发生错误: {e}")
        raise

def stock_selection(
    markets: Optional[List[str]] = None,
    min_price: float = 0.0,
    page: int = 1,
    page_size: int = 10000,
    source: str = "SELECT_SECURITIES",
    client: str = "WEB",
    extra_filters: Optional[str] = None
) -> pd.DataFrame:
    """
    东方财富网-个股-选股器
    https://data.eastmoney.com/xuangu/
    
    :param markets: 市场类别列表，例如 ["上交所主板", "深交所主板"]。默认为 ["上交所主板", "深交所主板", "深交所创业板"]
    :param min_price: 最低股价筛选条件。默认为 0.0
    :param page: 请求的页码。默认为 1
    :param page_size: 每页返回的数据量。默认为 10000
    :param source: 数据来源。默认为 "SELECT_SECURITIES"
    :param client: 客户端类型。默认为 "WEB"
    :param extra_filters: 额外的过滤条件字符串。默认为 None
    :return: 选股结果的DataFrame
    :rtype: pandas.DataFrame
    """
    cols = TABLE_BASE['columns']
    
    # 构建 'sty' 字符串，包含所有需要的字段
    sty_fields = [col_info['map'] for col_name, col_info in cols.items()]
    sty = ",".join(sty_fields)
    
    # 设置默认市场类别
    if markets is None:
        markets = ["上交所主板", "深交所主板", "深交所创业板"]
    
    # 构建过滤条件
    markets_quoted = ','.join(f'\"{market}\"' for market in markets)
    filter_conditions = f'(MARKET+in+({markets_quoted}))(NEW_PRICE>{min_price})'
    if extra_filters:
        filter_conditions += extra_filters
    
    # 请求URL和参数
    url = "https://data.eastmoney.com/dataapi/xuangu/list"
    params = {
        "sty": sty,
        "filter": filter_conditions,
        "p": page,
        "ps": page_size,
        "source": source,
        "client": client,
    }
    logger.info(f"请求参数: {params}")

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data_json = response.json()
        data = data_json.get("result", {}).get("data", [])
        # 处理每个数据记录
        # 获取当前时间
        current_time = datetime.datetime.now()
        for item in data:
            # 添加UPDATE_TIME字段
            item['UPDATE_TIME'] = current_time
            # 生成UNIQ_ID字段 (MAX_TRADE_DATE + SECURITY_CODE)
            item['UNIQ_ID'] = f"{item['MAX_TRADE_DATE']}{item['SECURITY_CODE']}"
        if not data:
            return pd.DataFrame()
        temp_df = pd.DataFrame(data)
    except requests.RequestException as e:
        logger.error(f"HTTP请求失败: {e}")
        return pd.DataFrame()
    except ValueError as e:
        logger.error(f"解析JSON失败: {e}")
        return pd.DataFrame()

    # 处理 'CONCEPT' 和 'STYLE' 列
    for field in ['CONCEPT', 'STYLE']:
        if field in temp_df.columns and temp_df[field].notna().any():
            temp_df[field] = temp_df[field].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

    # 数据类型转换
    for col_name, col_info in cols.items():
        field = col_info["map"]
        field_type = get_field_type_name(col_info["type"])
        if field in temp_df.columns:
            if field_type == 'numeric':
                temp_df[field] = pd.to_numeric(temp_df[field], errors="coerce")
            elif field_type == 'datetime':
                temp_df[field] = pd.to_datetime(temp_df[field], errors="coerce").dt.date

    return temp_df

# 获取综合选股数据并写入数据库
if __name__ == "__main__":
    try:
        # 获取最近一个交易日的数据
        df = stock_selection()
        # df = stock_selection()
        # 将数据写入数据库
        write_to_database(df, table_name='base')
    except Exception as e:
        logger.error(f"整个流程发生错误: {e}")
