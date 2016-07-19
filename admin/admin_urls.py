#!/usr/bin/env python3
# _*_coding:utf-8_*_
from admin.handler.companyHandler import AdminCompanyHandler, AdminCompanyAddHandler, AdminCompanyUpdateHandler, AdminCompanyDeleteHandler
from admin.handler.indexHandler import AdminIndexHandler
from admin.handler.loginHandler import AdminLoginHandler, AdminLogoutHandler
from admin.handler.priceHandler import AdminPriceHandler
from admin.handler.userHandler import AdminUserHandler, AdminUserAddHandler, AdminUserUpdateHandler, AdminUserDeleteHandler

admin_urls = [
    (r"/admin", AdminIndexHandler),
    (r"/login", AdminLoginHandler),
    (r"/logout", AdminLogoutHandler),

    (r"/admin/user", AdminUserHandler),
    (r"/admin/user/add", AdminUserAddHandler),
    (r"/admin/user/update", AdminUserUpdateHandler),
    (r"/admin/user/delete", AdminUserDeleteHandler),

    (r"/admin/company", AdminCompanyHandler),
    (r"/admin/company/add", AdminCompanyAddHandler),
    (r"/admin/company/update", AdminCompanyUpdateHandler),
    (r"/admin/company/delete", AdminCompanyDeleteHandler),

    (r"/admin/price", AdminPriceHandler),
]
