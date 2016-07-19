#!/usr/bin/env python3
# _*_coding:utf-8_*_
import hashlib
import traceback

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler
from setting import logger


class AdminCompanyHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        companys = []
        try:
            query = {}
            show = {"_id": 0}
            cursor = self.db.bijia_company.find(query, show)
            while (yield cursor.fetch_next):
                company = cursor.next_object()
                companys.append(company)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/company_list.html", companys=companys, res_msg=res_msg)


class AdminCompanyAddHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        company = {}
        self.render("admin/company_add.html", res_msg=res_msg, form_action="/admin/company/add", company=company)

    @gen.coroutine
    def post(self, *args, **kwargs):
        name = self.get_argument("name", "")
        code = self.get_argument("code", "")
        address = self.get_argument("address", "")
        email = self.get_argument("email", "")
        tell_phone = self.get_argument("tell_phone", "")
        website = self.get_argument("website", "")
        try:
            company_dict = {
                "name": name,
                "code": code,
                "address": address,
                "email": email,
                "tell_phone": tell_phone,
                "website": website,
            }
            query = {"code": code}
            yield self.db.bijia_company.update(query, company_dict, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/company")


class AdminCompanyUpdateHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        company = {}
        try:
            code = self.get_argument("code", "")
            query = {"code": code}
            show = {"_id": 0}
            company = yield self.db.bijia_company.find_one(query, show)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/company_add.html", res_msg=res_msg, form_action="/admin/company/add", company=company)

    @gen.coroutine
    def post(self, *args, **kwargs):
        name = self.get_argument("name", "")
        code = self.get_argument("code", "")
        address = self.get_argument("address", "")
        email = self.get_argument("email", "")
        tell_phone = self.get_argument("tell_phone", "")
        website = self.get_argument("website", "")
        try:
            company_dict = {
                "name": name,
                "code": code,
                "address": address,
                "email": email,
                "tell_phone": tell_phone,
                "website": website,
            }
            query = {"code": code}
            yield self.db.bijia_company.update(query, company_dict, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/company")


class AdminCompanyDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            code = self.get_argument("code", "")
            query = {"code": code}
            self.db.bijia_company.remove(query)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/company")
