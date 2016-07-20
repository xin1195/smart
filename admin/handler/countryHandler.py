#!/usr/bin/env python3
# _*_coding:utf-8_*_
import traceback

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler
from setting import logger


class AdminCountryHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        countrys = []
        num = int(self.get_argument("num", 15))
        page = int(self.get_argument("page", 1))
        total_count = 0
        try:
            query = {}
            show = {"_id": 0}
            cursor = self.db.bijia_country.find(query, show).skip((page - 1) * num).limit(num)
            while (yield cursor.fetch_next):
                country = cursor.next_object()
                countrys.append(country)
            total_count = yield self.db.bijia_country.find().count()
        except:
            logger.error(traceback.format_exc())
        self.render("admin/country_list.html", countrys=countrys, res_msg=res_msg, total_count=total_count, page=page,  num=num)


class AdminCountryAddHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        country = {}
        self.render("admin/country_add.html", res_msg=res_msg, form_action="/admin/country/add", country=country)

    @gen.coroutine
    def post(self, *args, **kwargs):
        abbreviate = self.get_argument("abbreviate", "")
        area = self.get_argument("area", "")
        name_zh = self.get_argument("name_zh", "")
        name_en = self.get_argument("name_en", "")

        try:
            country_dict = {
                "abbreviate": abbreviate,
                "area": area,
                "name_zh": name_zh,
                "name_en": name_en,
            }
            query = {"abbreviate": abbreviate}
            yield self.db.bijia_country.update(query, country_dict, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/country")


class AdminCountryUpdateHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        country = {}
        try:
            abbreviate = self.get_argument("abbreviate", "")
            query = {"abbreviate": abbreviate}
            show = {"_id": 0}
            country = yield self.db.bijia_country.find_one(query, show)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/country_add.html", res_msg=res_msg, form_action="/admin/country/add", country=country)

    @gen.coroutine
    def post(self, *args, **kwargs):
        abbreviate = self.get_argument("abbreviate", "")
        area = self.get_argument("area", "")
        name_zh = self.get_argument("name_zh", "")
        name_en = self.get_argument("name_en", "")
        try:
            country_dict = {
                "abbreviate": abbreviate,
                "area": area,
                "name_zh": name_zh,
                "name_en": name_en,
            }
            query = {"abbreviate": abbreviate}
            yield self.db.bijia_country.update(query, {"$set": country_dict}, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/country")


class AdminCountryDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            code = self.get_argument("code", "")
            query = {"code": code}
            self.db.bijia_country.remove(query)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/country")
