#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/5/25

# 基类
import tornado.web

from setting import client


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.db = client.smartSearch

    def data_received(self, chunk):
        pass

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def on_finish(self):
        pass
