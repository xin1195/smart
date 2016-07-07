#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/6/2
import json
import time
import traceback

import tornado.web
from tornado import gen

from setting import client, logger, g_redis_db


class BaseApiHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def check_xsrf_cookie(self):
        pass

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.callback = self.get_argument("callback", "")
        self.start_time = time.time()
        self.db = client.smartSearch
        self.redis_db = g_redis_db

    def change_to_jsonp(self, results=[], page_info={}):
        """
        将返回的结果根据是否存在 callback 参数转换成jsonp格式，主要是提供给网站使用
        :param page_info:
        :param results:
        :return: 将转换后的结果返回给页面
        """
        return_data = {
            "code": 200,
            "time": time.time() - self.start_time,
            "results": results,
        }
        if page_info:
            return_data["pageInfo"] = page_info
        if self.callback:
            return_data = str(self.callback) + "(" + json.dumps(return_data) + ")"
        self.write(return_data)
        self.finish()

    @gen.coroutine
    def get_results_redis(self):
        results = []
        exists_redis = yield gen.Task(self.redis_db.exists, self.request.uri)
        if exists_redis:
            data = yield gen.Task(self.redis_db.get, self.request.uri, )
            data_dict = eval(data)
            results = data_dict.get("results")
        return results

    def write_error(self, status_code, **kwargs):
        logger.error(traceback.format_exc())
        return_data = {
            "code": status_code,
            "time": time.time() - self.start_time,
            "results": []
        }
        self.write(return_data)
        self.finish()
