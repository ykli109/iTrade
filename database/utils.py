# 添加项目根目录到Python路径
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import SQLAlchemyError
from database.config import DB_CONFIGS  # 假设我们有多个数据库配置
from utils.log import initLog
import pandas as pd
from datetime import datetime

# 初始化日志
logger = initLog(log_filename='database_utils.log')

# 全局引擎字典
_engines = {}
def get_engine(db_name='default'):
    """
    创建并返回SQLAlchemy引擎（多数据库支持）。
    :param db_name: 数据库配置名称
    :return: SQLAlchemy引擎实例
    """
    global _engines
    if db_name not in _engines:
        if db_name not in DB_CONFIGS:
            logger.error(f"未找到数据库配置: {db_name}")
            return None
        
        config = DB_CONFIGS[db_name]
        db_url = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset={config['charset']}"
        
        try:
            _engines[db_name] = create_engine(db_url)
            logger.info(f"SQLAlchemy 引擎创建成功: {db_name}")
        except SQLAlchemyError as e:
            logger.error(f"创建引擎失败 {db_name}: {e}")
            return None
    
    return _engines[db_name]

# 插入DataFrame到数据库
def insert_db_from_df(data, table_name, db_name='default'):
    """
    将DataFrame数据插入或更新到指定的数据库表中，并添加updated_at字段。
    :param data: 要插入的DataFrame
    :param table_name: 目标表名
    :param db_name: 数据库名称
    """
    engine = get_engine(db_name)
    if engine is None:
        logger.error(f"无法获取数据库引擎 {db_name}，插入操作中止。")
        return
    
    # 检查DataFrame是否为空
    if data.empty:
        logger.warning("DataFrame为空，无法进行插入操作。")
        return

    try:
        with engine.connect() as connection:
            with connection.begin():
                # 检查表是否存在
                inspector = inspect(engine)
                if not inspector.has_table(table_name):
                    # 如果表不存在,直接创建表并插入数据
                    data.to_sql(table_name, connection, index=False)
                    logger.info(f"创建表 {table_name} 并插入数据成功")
                    return

                # 根据uniq_id判断，当前表中是否存在与data中重复的数据，如果存在，则批量删除数据
                # 获取data中的所有uniq_id
                if 'uniq_id' in data.columns:
                    uniq_ids = tuple(data['uniq_id'].tolist())
                    if len(uniq_ids) == 1:
                        # 如果只有一个值,需要特殊处理语法
                        delete_sql = f"DELETE FROM {table_name} WHERE uniq_id = '{uniq_ids[0]}'"
                    else:
                        delete_sql = f"DELETE FROM {table_name} WHERE uniq_id IN {uniq_ids}"
                    connection.execute(text(delete_sql))
                    logger.info(f"删除表 {table_name} 中的重复数据成功")

                # 插入新数据
                data.to_sql(table_name, connection, if_exists='append', index=False)
                logger.info(f"向表 {table_name} 插入新数据成功")

    except SQLAlchemyError as e:
        logger.error(f"在插入或更新数据到表 `{table_name}` (数据库: {db_name}) 时发生错误: {str(e)}")
