#!/usr/bin/env python3
import tornado.web

from admin.handler.baseHandler import BaseHandler


class AdminIndexHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render("admin/index.html")




