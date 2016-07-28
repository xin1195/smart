#!/usr/bin/env python3
# _*_coding:utf-8_*_
import traceback

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler
from common.authLib import auth_permissions
from setting import logger


class AdminNodeHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        nodes = []
        num = int(self.get_argument("num", 15))
        page = int(self.get_argument("page", 1))
        total_count = 0
        try:
            query = {}
            show = {"_id": 0}
            cursor = self.db.sys_node.find(query, show).skip((page - 1) * num).limit(num)
            while (yield cursor.fetch_next):
                user = cursor.next_object()
                nodes.append(user)
            total_count = yield self.db.sys_node.find().count()
        except:
            logger.error(traceback.format_exc())
        self.render("admin/sys_node_list.html", nodes=nodes, res_msg=res_msg, total_count=total_count, page=page, num=num)


class AdminNodeAddHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        node = {}
        self.render("admin/sys_node_add.html", res_msg=res_msg, form_action="/admin/node/add", node=node)

    @auth_permissions
    @gen.coroutine
    def post(self, *args, **kwargs):
        node_id = self.get_argument("node_id", "")
        node_name = self.get_argument("node_name", "")
        try:
            node_dict = {
                "node_id": node_id,
                "node_name": node_name,
            }
            query = {"node_id": node_id}
            yield self.db.sys_node.update(query, node_dict, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/node")


class AdminNodeUpdateHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        node = {}
        try:
            node_id = self.get_argument("node_id", "")
            query = {"node_id": node_id}
            show = {"_id": 0}
            node = yield self.db.sys_node.find_one(query, show)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/sys_node_add.html", node=node, res_msg=res_msg, form_action="/admin/node/update")

    @auth_permissions
    @gen.coroutine
    def post(self, *args, **kwargs):
        node_id = self.get_argument("node_id", "")
        node_name = self.get_argument("node_name", "")
        try:
            node_dict = {
                "node_id": node_id,
                "node_name": node_name,
            }
            query = {"node_id": node_id}
            yield self.db.sys_node.update(query, {"$set": node_dict}, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/node")


class AdminNodeDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    @auth_permissions
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            node_id = self.get_argument("node_id", "")
            query = {"node_id": node_id}
            self.db.sys_node.remove(query)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/node")
