#!/usr/bin/env python3
# _*_coding:utf-8_*_
import hashlib
import traceback

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler
from setting import logger


class AdminUserHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        users = []
        try:
            query = {}
            show = {"_id": 0}
            cursor = self.db.sys_user.find(query, show)
            while (yield cursor.fetch_next):
                user = cursor.next_object()
                users.append(user)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/user_list.html", users=users, res_msg=res_msg)


class AdminUserAddHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        user = {}
        self.render("admin/user_add.html", res_msg=res_msg, form_action="/admin/user/add", user=user)

    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        email = self.get_argument("email", "")
        tell_phone = self.get_argument("tell_phone", "")
        try:
            salt = hashlib.md5(username.encode('utf-8')).hexdigest()
            hash_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
            user_dict = {
                "username": username,
                "password": hash_password,
                "email": email,
                "tell_phone": tell_phone,
            }
            query = {"username": username}
            yield self.db.sys_user.update(query, user_dict, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/user")


class AdminUserUpdateHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        user = {}
        try:
            username = self.get_argument("username", "")
            query = {"username": username}
            show = {"_id": 0}
            user = yield self.db.sys_user.find_one(query, show)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/user_add.html", user=user, res_msg=res_msg, form_action="/admin/user/update")

    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        email = self.get_argument("email", "")
        tell_phone = self.get_argument("tell_phone", "")
        try:
            user_dict = {
                "username": username,
                "email": email,
                "tell_phone": tell_phone,
            }
            if password:
                salt = hashlib.md5(username.encode('utf-8')).hexdigest()
                hash_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
                user_dict["password"] = hash_password
            query = {"username": username}
            yield self.db.sys_user.update(query, {"$set": user_dict}, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/user")


class AdminUserDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            username = self.get_argument("username", "")
            query = {"username": username}
            self.db.sys_user.remove(query)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/user")
