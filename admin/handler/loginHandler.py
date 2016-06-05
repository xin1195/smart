#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/5/25
import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler


class AdminLoginHandler(BaseHandler):
    def get(self):
        self.render("admin/login.html")

    @gen.coroutine
    def post(self):
        username = self.get_argument("username", default="")
        password = self.get_argument("password", default="")
        if username != "" and password != "":
            user = yield self.db.user.find_one({"username": username, "password": password})
            if user:
                self.set_secure_cookie("user", username)
                self.redirect("/admin")
        self.redirect("/admin/login")


class AdminLogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.set_secure_cookie("user", "")
        self.render("admin/login.html")

