# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)  # 修改为insert以确保优先搜索项目根目录

import time
import datetime
from utils.log import initLog

def main():
    logger = initLog(log_filename='execute_daily_job.log')  # 指定日志文件名
    
    start = time.time()
    _start = datetime.datetime.now()
    logger.info("######## 任务执行时间: %s #######" % _start.strftime("%Y-%m-%d %H:%M:%S.%f"))
    
    from database.utils import get_engine
    
    # 初始化默认数据库
    default_engine = get_engine()
    if default_engine:
        logger.info("成功初始化默认数据库连接")
    else:
        logger.error("初始化默认数据库连接失败")

    
    logger.info("######## 完成任务, 使用时间: %s 秒 #######" % (time.time() - start))

# main函数入口
if __name__ == '__main__':
    main()
