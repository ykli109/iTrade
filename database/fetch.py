# 添加项目根目录到Python路径
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import pandas as pd
import requests
from typing import List, Optional
from utils.log import initLog
from data.cn_stock_selection import TABLE_CN_STOCK_SELECTION
from data.utils import get_field_type_name

# 初始化日志
logger = initLog(log_filename='database_fetch.log')

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
    cols = TABLE_CN_STOCK_SELECTION['columns']
    
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
        "client": client
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data_json = response.json()
        data = data_json.get("result", {}).get("data", [])
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
