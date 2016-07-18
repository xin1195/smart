#!/usr/bin/env python3
# _*_coding:utf-8_*_
from admin.handler.indexHandler import AdminIndexHandler
from admin.handler.loginHandler import AdminLoginHandler, AdminLogoutHandler
from admin.handler.userHandler import AdminUserHandler, AdminUserAddHandler, AdminUserUpdateHandler, \
    AdminUserDeleteHandler

admin_urls = [
    (r"/admin", AdminIndexHandler),
    (r"/login", AdminLoginHandler),
    (r"/logout", AdminLogoutHandler),

    (r"/admin/user", AdminUserHandler),
    (r"/admin/user/add", AdminUserAddHandler),
    (r"/admin/user/update", AdminUserUpdateHandler),
    (r"/admin/user/delete", AdminUserDeleteHandler),
]
