#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator 
# Time 2016/7/25.
from tornado import gen
from setting import logger, g_py_client
import traceback

pyDB = g_py_client.ioswallpaper


@gen.coroutine
def check_auth_sync(self):
    try:
        node_id = self.request.uri.split("?")[0]
        # 查询用户属于哪些角色
        role_ids = []
        query = {"username": self.get_secure_cookie("user").decode('utf-8')}
        show = {"_id": 0}
        cursor = self.db.sys_user_role.find(query, show)
        while (yield cursor.fetch_next):
            sys_user_role = cursor.next_object()
            role_ids.append(sys_user_role.get("role_id", ""))
        # 查询这些角色有哪些权限
        node_ids = set()
        query = {"role_id": {"$in": role_ids}}
        show = {"_id": 0}
        cursor = self.db.sys_role_node.find(query, show)
        while (yield cursor.fetch_next):
            sys_role_node = cursor.next_object()
            node_ids.add(sys_role_node.get("node_id", ""))
        if node_id in node_ids:
            return 1
        else:
            return 0
    except:
        logger.error(traceback.format_exc())
        return 0


def check_auth(self):
    try:
        node_id = self.request.uri.split("?")[0]
        # 查询用户属于哪些角色
        role_ids = []
        query = {"username": self.get_secure_cookie("user").decode('utf-8')}
        show = {"_id": 0}
        sys_user_roles = pyDB.sys_user_role.find(query, show)
        for sys_user_role in sys_user_roles:
            role_ids.append(sys_user_role.get("role_id", ""))
        # 查询这些角色有哪些权限
        node_ids = set()
        query = {"role_id": {"$in": role_ids}}
        show = {"_id": 0}
        sys_role_nodes = pyDB.sys_role_node.find(query, show)
        for sys_role_node in sys_role_nodes:
            node_ids.add(sys_role_node.get("node_id", ""))
        if node_id in node_ids:
            return 1
        else:
            return 0
    except:
        logger.error(traceback.format_exc())
        return 0
