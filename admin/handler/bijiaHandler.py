#!/usr/bin/env python3
# _*_coding:utf-8_*_
import traceback

import tornado.web
from tornado import gen

from admin.handler.baseHandler import BaseHandler
from setting import logger


class AdminBijiaHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        res_msg = ""
        prices = []
        num = int(self.get_argument("num", 15))
        page = int(self.get_argument("page", 1))
        total_count = 0
        self.render("admin/bijia_list.html", prices=prices, res_msg=res_msg, total_count=total_count, page=page,
                    num=num)

    @tornado.web.authenticated
    @gen.coroutine
    def post(self, *args, **kwargs):
        res_msg = ""
        prices = []
        num = int(self.get_argument("num", 15))
        page = int(self.get_argument("page", 1))
        starting_place = self.get_argument("starting_place", "")
        destination = self.get_argument("destination", "")
        max_length = self.get_argument("max_length", 0)
        max_width = self.get_argument("max_width", 0)
        max_height = self.get_argument("max_height", 0)
        weight = self.get_argument("weight", "")
        is_liquid = self.get_argument("is_liquid", "")
        is_electric = self.get_argument("is_electric", "")
        total_count = 0
        try:
            if weight:
                weight = float(weight)
            query = {
                "starting_place": starting_place,
                "destination": destination,
            }
            show = {"_id": 0}
            cursor = self.db.bijia_price.find(query, show).skip((page - 1) * num).limit(num)
            while (yield cursor.fetch_next):
                price = cursor.next_object()
                price["total_price"] = float(price["register_price"]) + float(price["freight"]) * weight
                prices.append(price)
            total_count = yield self.db.bijia_price.find(query, show).count()
        except:
            logger.error(traceback.format_exc())
        self.render("admin/bijia_list.html", prices=prices, res_msg=res_msg, total_count=total_count, page=page,
                    num=num)
