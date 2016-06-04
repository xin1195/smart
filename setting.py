#!/usr/bin/env python3
# _*_coding:utf-8_*_
import os
import motor.motor_asyncio

# 设置文件配置
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="bZJc2sWbQLKoscdGkHn/VytuyfgXwQt8S0R0kRvJ5/xJ89E=",
    login_url="/admin/login",
    xsrf_cookies=True,
    debug=True,

)

# 设置mongodb的连接
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://112.74.204.250:27017')

