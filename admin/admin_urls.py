#!/usr/bin/env python3
# _*_coding:utf-8_*_
from admin.handler.indexHandler import AdminIndexHandler
from admin.handler.loginHandler import AdminLoginHandler, AdminLogoutHandler

admin_urls = [
    (r"/admin", AdminIndexHandler),
    (r"/admin/login", AdminLoginHandler),
    (r"/admin/logout", AdminLogoutHandler),

]
