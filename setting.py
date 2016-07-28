#!/usr/bin/env python3
# _*_coding:utf-8_*_
import os

import motor.motor_tornado
import tornadoredis
from pymongo import MongoClient

from common.logManageLib import get_logger

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="bZJc2sWbQLKoscdGkHn/VytuyfgXwQt8S0R0kRvJ5/xJ89E=",
    login_url="/login",
    xsrf_cookies=True,
    debug=True,

)

# 设置mongodb的连接
client = motor.motor_tornado.MotorClient('mongodb://112.74.204.250:27017')
# 获取数据库连接
g_py_client = MongoClient("mongodb://112.74.204.250:27017")

# 设置redis的连接
g_redis_db = tornadoredis.Client(host='112.74.204.250', port=6379, password=None, selected_db=1)

g_redis_time_5m = 5 * 60
g_redis_time_10m = 10 * 60
g_redis_time_30m = 30 * 60
g_redis_time_1h = 1 * 60 * 60
g_redis_time_2h = 2 * 60 * 60
g_redis_time_5h = 5 * 60 * 60
g_redis_time_1d = 24 * 60 * 60
g_redis_time_1w = 7 * 24 * 60 * 60

# 日志配置
logger = get_logger(strFileName="smartSearch.log", debug=20, showStreamLog=True, saveLogPath=None)

# domain 域名配置
domain = "http://www.liuhub.com/"
# domain = "http://127.0.0.1:8000/"




