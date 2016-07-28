#!/usr/bin/env python3
# _*_coding:utf-8_*_
import traceback

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler
from common.authLib import auth_permissions
from setting import logger


class AdminRoleHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        roles = []
        num = int(self.get_argument("num", 15))
        page = int(self.get_argument("page", 1))
        total_count = 0
        try:
            query = {}
            show = {"_id": 0}
            cursor = self.db.sys_role.find(query, show).skip((page - 1) * num).limit(num)
            while (yield cursor.fetch_next):
                user = cursor.next_object()
                roles.append(user)
            total_count = yield self.db.sys_role.find().count()
        except:
            logger.error(traceback.format_exc())
        self.render("admin/sys_role_list.html", roles=roles, res_msg=res_msg, total_count=total_count, page=page, num=num)


class AdminRoleAddHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        role = {}
        self.render("admin/sys_role_add.html", res_msg=res_msg, form_action="/admin/role/add", role=role)

    @auth_permissions
    @gen.coroutine
    def post(self, *args, **kwargs):
        role_id = self.get_argument("role_id", "")
        role_name = self.get_argument("role_name", "")
        try:
            role_dict = {
                "role_id": role_id,
                "role_name": role_name,
            }
            query = {"role_id": role_id}
            yield self.db.sys_role.update(query, role_dict, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/role")


class AdminRoleUpdateHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        role = {}
        try:
            role_id = self.get_argument("role_id", "")
            query = {"role_id": role_id}
            show = {"_id": 0}
            role = yield self.db.sys_role.find_one(query, show)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/sys_role_add.html", role=role, res_msg=res_msg, form_action="/admin/role/update")

    @auth_permissions
    @gen.coroutine
    def post(self, *args, **kwargs):
        role_id = self.get_argument("role_id", "")
        role_name = self.get_argument("role_name", "")
        try:
            role_dict = {
                "role_id": role_id,
                "role_name": role_name,
            }
            query = {"role_id": role_id}
            yield self.db.sys_role.update(query, {"$set": role_dict}, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/user")


class AdminRoleDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            role_id = self.get_argument("role_id", "")
            query = {"role_id": role_id}
            self.db.sys_role.remove(query)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/role")
