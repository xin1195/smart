#!/usr/bin/env python3
# _*_coding:utf-8_*_
import traceback

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler
from setting import logger


class AdminPriceHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        prices = []
        num = int(self.get_argument("num", 15))
        page = int(self.get_argument("page", 1))
        total_count = 0
        try:
            query = {}
            show = {"_id": 0}
            cursor = self.db.bijia_price.find(query, show)
            while (yield cursor.fetch_next):
                price = cursor.next_object()
                prices.append(price)
            total_count = yield self.db.bijia_price.find().count()
        except:
            logger.error(traceback.format_exc())
        self.render("admin/price_list.html", prices=prices, res_msg=res_msg, total_count=total_count, page=page,  num=num)


class AdminPriceAddHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        price = {}
        self.render("admin/price_add.html", res_msg=res_msg, form_action="/admin/price/add", price=price)

    @gen.coroutine
    def post(self, *args, **kwargs):
        line_name = self.get_argument("line_name", "")
        line_code = self.get_argument("line_code", "")
        company_code = self.get_argument("company_code", "")
        starting_place = self.get_argument("starting_place", "")
        destination = self.get_argument("destination", "")
        register_price = self.get_argument("register_price", "")
        freight = self.get_argument("freight", "")
        arrival_time = self.get_argument("arrival_time", "")
        is_electric = self.get_argument("is_electric", "")
        is_liquid = self.get_argument("is_liquid", "")
        arrival_rate = self.get_argument("arrival_rate", "")
        max_weight = self.get_argument("max_weight", "")
        condition = self.get_argument("condition", "")
        special_requirement = self.get_argument("special_requirement", "")
        remarks = self.get_argument("remarks", "")
        statement = self.get_argument("statement", "")
        try:
            price_dict = {
                "line_name": line_name,
                "line_code": line_code,
                "company_code": company_code,
                "starting_place": starting_place,
                "destination": destination,
                "register_price": register_price,
                "freight": freight,
                "arrival_time": arrival_time,
                "is_electric": is_electric,
                "is_liquid": is_liquid,
                "arrival_rate": arrival_rate,
                "max_weight": max_weight,
                "condition": condition,
                "special_requirement": special_requirement,
                "remarks": remarks,
                "statement": statement,
            }
            query = {"line_code": line_code}
            yield self.db.bijia_price.update(query, price_dict, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/price")


class AdminPriceUpdateHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        price = {}
        try:
            line_code = self.get_argument("line_code", "")
            query = {"line_code": line_code}
            show = {"_id": 0}
            price = yield self.db.bijia_price.find_one(query, show)
        except:
            logger.error(traceback.format_exc())
        self.render("admin/price_add.html", res_msg=res_msg, form_action="/admin/price/add", price=price)

    @gen.coroutine
    def post(self, *args, **kwargs):
        line_name = self.get_argument("line_name", "")
        line_code = self.get_argument("line_code", "")
        company_code = self.get_argument("company_code", "")
        starting_place = self.get_argument("starting_place", "")
        destination = self.get_argument("destination", "")
        register_price = self.get_argument("register_price", "")
        freight = self.get_argument("freight", "")
        arrival_time = self.get_argument("arrival_time", "")
        is_electric = self.get_argument("is_electric", "")
        is_liquid = self.get_argument("is_liquid", "")
        arrival_rate = self.get_argument("arrival_rate", "")
        max_weight = self.get_argument("max_weight", "")
        condition = self.get_argument("condition", "")
        special_requirement = self.get_argument("special_requirement", "")
        remarks = self.get_argument("remarks", "")
        statement = self.get_argument("statement", "")
        try:
            price_dict = {
                "line_name": line_name,
                "line_code": line_code,
                "company_code": company_code,
                "starting_place": starting_place,
                "destination": destination,
                "register_price": register_price,
                "freight": freight,
                "arrival_time": arrival_time,
                "is_electric": is_electric,
                "is_liquid": is_liquid,
                "arrival_rate": arrival_rate,
                "max_weight": max_weight,
                "condition": condition,
                "special_requirement": special_requirement,
                "remarks": remarks,
                "statement": statement,
            }
            query = {"line_code": line_code}
            yield self.db.bijia_price.update(query, {"$set": price_dict}, upsert=True)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/price")


class AdminPriceDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            line_code = self.get_argument("line_code", "")
            query = {"line_code": line_code}
            self.db.bijia_price.remove(query)
        except:
            logger.error(traceback.format_exc())
        self.redirect("/admin/price")
