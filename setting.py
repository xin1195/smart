#!/usr/bin/env python3
# _*_coding:utf-8_*_
import os
import motor.motor_tornado

from comon.handler.LogManage import get_logger

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="bZJc2sWbQLKoscdGkHn/VytuyfgXwQt8S0R0kRvJ5/xJ89E=",
    login_url="/admin/login",
    xsrf_cookies=True,
    debug=True,

)

# 设置mongodb的连接
client = motor.motor_tornado.MotorClient('mongodb://112.74.204.250:27017')
dict_app_country = {
    # 中国
    "zh_hant_hk": "CN", "zh_hans_sg": "CN", "zh_hans_hk": "CN", "zh_hans": "CN", "zh": "CN", "zh_hans_cn": "CN", "zh_hant": "CN",
    "zh_hant_tw": "CN", "zh_hant_mo": "CN", "zh_hans_mo": "CN",
    # 美国
    "us": "US",
    "en": "US",
    # 阿拉伯
    'ar_ye': "SA", 'ar_eg': "SA", 'ar_sa': "SA", 'ar_sd': "SA", 'ar_ly': "SA", 'ar_om': "SA", 'ar_ma': "SA", 'ar_tn': "SA", 'ar_jo': "SA",
    'ar_kw': "SA", 'ar_qa': "SA", 'ar_lb': "SA", 'ar_iq': "SA", 'ar_bh': "SA", 'ar': "SA", 'ar_ae': "SA", 'ar_dz': "SA", 'ar_sy': "SA",
}

logger = get_logger(strFileName="smartSearch.log",
                    debug=30,
                    showStreamLog=True,
                    saveLogPath=None)
