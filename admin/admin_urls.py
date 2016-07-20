#!/usr/bin/env python3
# _*_coding:utf-8_*_
from admin.handler.bijiaHandler import AdminBijiaHandler
from admin.handler.companyHandler import AdminCompanyHandler, AdminCompanyAddHandler, AdminCompanyUpdateHandler, AdminCompanyDeleteHandler
from admin.handler.countryHandler import AdminCountryAddHandler, AdminCountryUpdateHandler, AdminCountryDeleteHandler
from admin.handler.countryHandler import AdminCountryHandler
from admin.handler.indexHandler import AdminIndexHandler
from admin.handler.loginHandler import AdminLoginHandler, AdminLogoutHandler
from admin.handler.priceHandler import AdminPriceHandler, AdminPriceAddHandler, AdminPriceUpdateHandler, AdminPriceDeleteHandler
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

    (r"/admin/country", AdminCountryHandler),
    (r"/admin/country/add", AdminCountryAddHandler),
    (r"/admin/country/update", AdminCountryUpdateHandler),
    (r"/admin/country/delete", AdminCountryDeleteHandler),

    (r"/admin/price", AdminPriceHandler),
    (r"/admin/price/add", AdminPriceAddHandler),
    (r"/admin/price/update", AdminPriceUpdateHandler),
    (r"/admin/price/delete", AdminPriceDeleteHandler),

    (r"/admin/bijia", AdminBijiaHandler),

]
