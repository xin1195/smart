#!/usr/bin/env python3
# _*_coding:utf-8_*_
from home.handler.indexHandler import HomeIndexHandler, HomeIndex2Handler, HomeIndex3Handler, HomeIndex4Handler
from home.handler.webSocketHandler import UserSocketHandler

home_urls = [
    (r"/", HomeIndexHandler),
    (r"/index", HomeIndexHandler),
    (r"/index2", HomeIndex2Handler),
    (r"/index3", HomeIndex3Handler),
    (r"/index4", HomeIndex4Handler),
    (r"/userSocket", UserSocketHandler),

]
