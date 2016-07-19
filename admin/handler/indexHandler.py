#!/usr/bin/env python3
import tornado.web

from admin.handler.baseHandler import BaseHandler


class AdminIndexHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("admin/index.html")




