#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator 
# Time 2016/7/27.


from common.commonLib import check_auth


# 权限装饰器
def auth_permissions(func):
    def inner(self, *args, **kwargs):
        ret = check_auth(self)
        if ret:
            return func(self, *args, **kwargs)
        else:
            self.render("admin/403.html")
    return inner
