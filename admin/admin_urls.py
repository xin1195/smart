#!/usr/bin/env python3
# _*_coding:utf-8_*_
from tornado import web
from admin.handler.bijiaHandler import AdminBijiaHandler
from admin.handler.companyHandler import AdminCompanyHandler, AdminCompanyAddHandler, AdminCompanyUpdateHandler, AdminCompanyDeleteHandler
from admin.handler.countryHandler import AdminCountryAddHandler, AdminCountryUpdateHandler, AdminCountryDeleteHandler
from admin.handler.countryHandler import AdminCountryHandler
from admin.handler.loginHandler import AdminLoginHandler, AdminLogoutHandler
from admin.handler.nodeHandler import AdminNodeHandler, AdminNodeAddHandler, AdminNodeUpdateHandler, \
    AdminNodeDeleteHandler
from admin.handler.priceHandler import AdminPriceHandler, AdminPriceAddHandler, AdminPriceUpdateHandler, AdminPriceDeleteHandler
from admin.handler.roleHandler import AdminRoleHandler, AdminRoleAddHandler, AdminRoleUpdateHandler, \
    AdminRoleDeleteHandler
from admin.handler.userHandler import AdminUserHandler, AdminUserAddHandler, AdminUserUpdateHandler, AdminUserDeleteHandler

admin_urls = [
    # 首页 登录 登出
    web.URLSpec(r"/", AdminBijiaHandler, name="index"),
    web.URLSpec(r"/admin", AdminBijiaHandler, name="admin"),
    web.URLSpec(r"/login", AdminLoginHandler, name="login"),
    web.URLSpec(r"/logout", AdminLogoutHandler, name="logout"),
    # 用户管理
    web.URLSpec(r"/admin/user", AdminUserHandler, name="admin_user"),
    web.URLSpec(r"/admin/user/add", AdminUserAddHandler, name="admin_user_add"),
    web.URLSpec(r"/admin/user/update", AdminUserUpdateHandler, name="admin_user_update"),
    web.URLSpec(r"/admin/user/delete", AdminUserDeleteHandler, name="admin_user_delete"),
    # 角色管理
    web.URLSpec(r"/admin/role", AdminRoleHandler, name="admin_role"),
    web.URLSpec(r"/admin/role/add", AdminRoleAddHandler, name="admin_role_add"),
    web.URLSpec(r"/admin/role/update", AdminRoleUpdateHandler, name="admin_role_update"),
    web.URLSpec(r"/admin/role/delete", AdminRoleDeleteHandler, name="admin_role_delete"),
    # 权限节点管理
    web.URLSpec(r"/admin/node", AdminNodeHandler, name="admin_node"),
    web.URLSpec(r"/admin/node/add", AdminNodeAddHandler, name="admin_node_add"),
    web.URLSpec(r"/admin/node/update", AdminNodeUpdateHandler, name="admin_node_update"),
    web.URLSpec(r"/admin/node/delete", AdminNodeDeleteHandler, name="admin_node_delete"),
    # 公司管理
    web.URLSpec(r"/admin/company", AdminCompanyHandler, name="admin_company"),
    web.URLSpec(r"/admin/company/add", AdminCompanyAddHandler, name="admin_company_add"),
    web.URLSpec(r"/admin/company/update", AdminCompanyUpdateHandler, name="admin_company_update"),
    web.URLSpec(r"/admin/company/delete", AdminCompanyDeleteHandler, name="admin_company_delete"),
    # 国家管理
    web.URLSpec(r"/admin/country", AdminCountryHandler, name="admin_country"),
    web.URLSpec(r"/admin/country/add", AdminCountryAddHandler, name="admin_country_add"),
    web.URLSpec(r"/admin/country/update", AdminCountryUpdateHandler, name="admin_country_update"),
    web.URLSpec(r"/admin/country/delete", AdminCountryDeleteHandler, name="admin_country_delete"),
    # 价格管理
    web.URLSpec(r"/admin/price", AdminPriceHandler, name="admin_price"),
    web.URLSpec(r"/admin/price/add", AdminPriceAddHandler, name="admin_price_add"),
    web.URLSpec(r"/admin/price/update", AdminPriceUpdateHandler, name="admin_price_update"),
    web.URLSpec(r"/admin/price/delete", AdminPriceDeleteHandler, name="admin_price_delete"),
    # 比价管理
    web.URLSpec(r"/admin/bijia", AdminBijiaHandler, name="admin_bijia"),

]
