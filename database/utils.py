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
    将DataFrame数据插入或更新到指定的数据库表中。
    :param data: 要插入的DataFrame
    :param table_name: 目标表名
    :param db_name: 数据库名称
    """
    engine = get_engine(db_name)
    if engine is None:
        logger.error(f"无法获取数据库引擎 {db_name}，插入操作中止。")
        return

    # 处理NaN值
    data = data.fillna(0)

    try:
        with engine.connect() as connection:
            # 批量查询现有的 date 和 code
            records = [(row['date'], row['code']) for _, row in data.iterrows()]

            # 使用 SQLAlchemy 的适当方式传递参数
            existing_records = connection.execute(
                text(f"SELECT date, code FROM {table_name} WHERE (date, code) IN :records"),
                {"records": records}
            ).fetchall()

            # 将查询结果转换为集合
            existing_ids_set = {(row[0], row[1]) for row in existing_records}

            # 分离需要更新和插入的数据
            updates = []
            inserts = []
            for _, row in data.iterrows():
                if (row['date'], row['code']) in existing_ids_set:
                    updates.append(row.to_dict())
                else:
                    inserts.append(row)

            # 批量更新
            if updates:
                # 获取DataFrame的列名
                columns = data.columns.tolist()
                # 构建更新语句
                update_stmt = f"""
                    UPDATE {table_name} 
                    SET {', '.join(f"{col} = :{col}" for col in columns if col not in ['date', 'code'])}
                    WHERE date = :date AND code = :code
                """
                connection.execute(text(update_stmt), updates)
                # 成功更新n条数据
                logger.info(f"成功更新 {len(updates)} 条数据到表 `{table_name}` (数据库: {db_name})。")

            # 批量插入
            if inserts:
                pd.DataFrame(inserts).to_sql(name=table_name, con=engine, if_exists='append', index=False, chunksize=2000)
                # 成功插入n条数据
                logger.info(f"成功插入 {len(inserts)} 条数据到表 `{table_name}` (数据库: {db_name})。")

    except SQLAlchemyError as e:
        logger.error(f"在插入或更新数据到表 `{table_name}` (数据库: {db_name}) 时发生错误: {str(e)}")

# 执行任意SQL语句
def execute_sql(sql, params=None, db_name='default'):
    """
    执行任意SQL语句。
    :param sql: 要执行的SQL语句
    :param params: SQL语句中的参数
    :param db_name: 数据库名称
    """
    engine = get_engine(db_name)
    if engine is None:
        logger.error(f"无法获取数据库引擎 {db_name}，SQL执行操作中止。")
        return

    try:
        with engine.connect() as conn:
            conn.execute(text(sql), params or {})
        logger.info(f"成功执行SQL语句 (数据库: {db_name}): {sql}")
    except SQLAlchemyError as e:
        logger.error(f"执行SQL语句失败 (数据库: {db_name}): {sql}，错误: {e}")

# 查询数据
def execute_sql_fetch(sql, params=None, db_name='default'):
    """
    执行查询SQL并返回结果。
    :param sql: 查询SQL语句
    :param params: SQL语句中的参数
    :param db_name: 数据库名称
    :return: 查询结果
    """
    engine = get_engine(db_name)
    if engine is None:
        logger.error(f"无法获取数据库引擎 {db_name}，查询操作中止。")
        return None

    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql), params or {})
            return result.fetchall()
    except SQLAlchemyError as e:
        logger.error(f"执行查询SQL失败 (数据库: {db_name}): {sql}，错误: {e}")
        return None

# 检查表是否存在
def check_table_exists(table_name, db_name='default'):
    """
    检查指定的表是否存在于数据库中。
    :param table_name: 表名
    :param db_name: 数据库名称
    :return: 存在返回True，否则返回False
    """
    engine = get_engine(db_name)
    if engine is None:
        logger.error(f"无法获取数据库引擎 {db_name}，检查表存在性操作中止。")
        return False

    inspector = inspect(engine)
    exists = inspector.has_table(table_name)
    logger.info(f"表 `{table_name}` 在数据库 {db_name} 中存在: {exists}")
    return exists
