#!/usr/bin/env python3
# _*_coding:utf-8_*_
from home.handler.indexHandler import HomeIndexHandler, HomeIndex2Handler

home_urls = [
    (r"/", HomeIndexHandler),
    (r"/index", HomeIndexHandler),
    (r"/index2", HomeIndex2Handler),

]
