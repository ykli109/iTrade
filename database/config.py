# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

DB_CONFIGS = {
    'default': {
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "password"),
        "database": os.getenv("DB_DATABASE", "itrade"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "charset": "utf8mb4"
    },
    # 'analytics': {
    #     "host": os.getenv("DB_ANALYTICS_HOST", "localhost"),
    #     "user": os.getenv("DB_ANALYTICS_USER", "root"),
    #     "password": os.getenv("DB_ANALYTICS_PASSWORD", "password"),
    #     "database": os.getenv("DB_ANALYTICS_DATABASE", "itrade_analytics"),
    #     "port": int(os.getenv("DB_ANALYTICS_PORT", 3306)),
    #     "charset": "utf8mb4"
    # }
}
