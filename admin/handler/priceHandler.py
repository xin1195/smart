#!/usr/bin/env python3
import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler


class AdminPriceHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("admin/price.html")

    @tornado.web.authenticated
    @gen.coroutine
    def post(self, *args, **kwargs):
        pass
