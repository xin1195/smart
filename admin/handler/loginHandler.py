#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/5/25
import motor.motor_tornado
from tornado import gen

from admin.handler.baseHandler import BaseHandler


class AdminLoginHandler(BaseHandler):
    def get(self):
        self.render("admin/sys_login.html")

    @gen.coroutine
    def post(self):
        username = self.get_argument("username", default="")
        password = self.get_argument("password", default="")
        if username != "" and password != "":
            db = motor.motor_tornado.MotorClient('mongodb://112.74.204.250:27017').smartSearch,
            document = {'username': username, 'password': password}
            db.users.insert(document)
        self.set_secure_cookie("user", username)
        self.redirect("/admin/")
