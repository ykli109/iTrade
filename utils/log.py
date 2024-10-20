import os
import sys
import logging

# 全局变量，用于跟踪日志是否已经初始化
_log_initialized = False

def initLog(log_filename='default.log'):
    """
    设置项目环境，将项目路径添加到环境变量，并配置日志。
    如果日志已经初始化，则直接返回现有的 logger。
    :param log_filename: 日志文件名
    :return: 配置好的 logger 对象
    """
    global _log_initialized

    # 如果日志已经初始化，直接返回现有的 logger
    if _log_initialized:
        return logging.getLogger()

    # 在项目运行时，临时将项目路径添加到环境变量
    cpath_current = os.path.dirname(os.path.dirname(__file__))
    cpath = os.path.abspath(os.path.join(cpath_current, os.pardir))
    sys.path.append(cpath)
    
    # 设置日志路径
    log_path = os.path.join(cpath_current, 'log')
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    
    # 配置日志
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        filename=os.path.join(log_path, log_filename),
        level=logging.INFO
    )
    
    # 标记日志已初始化
    _log_initialized = True
    
    return logging.getLogger()
