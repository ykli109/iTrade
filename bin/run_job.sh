#!/bin/bash

# 获取脚本所在目录的父目录(假设为项目根目录)
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
echo PROJECT_ROOT: $PROJECT_ROOT

# 执行Python脚本
python3 "$PROJECT_ROOT/job/execute_daily_job.py"

# 退出脚本
exit 0  # 以状态码0正常退出
