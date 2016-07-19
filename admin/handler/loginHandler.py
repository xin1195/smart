#!/usr/bin/env python3
# _*_coding:utf-8_*_
import hashlib

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler


class AdminLoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("admin/sys_login.html")

    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument("username", default="")
        password = self.get_argument("password", default="")
        if username != "" and password != "":
            salt = hashlib.md5(username.encode('utf-8')).hexdigest()
            hash_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
            query = {"username": username, "password": hash_password}
            show = {"_id": 0, "username": 1, "password": 1}
            user = yield self.db.sys_user.find_one(query, show)
            if user:
                self.set_secure_cookie("user", username)
                self.redirect("/admin")
            else:
                self.redirect("/login")
        else:
            self.redirect("/login")


class AdminLogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.set_secure_cookie("user", "")
        self.redirect("/login")