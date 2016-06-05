#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/6/2
import time
from tornado_json.requesthandlers import APIHandler

from setting import client, dict_app_country


class BaseApiHandler(APIHandler):
    def data_received(self, chunk):
        pass

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.start_time = time.time()
        self.db = client.smartSearch
        self.device = self.get_argument("device", 1)
        self.language = self.get_argument("language", "en")
        self._from = self.get_argument("_from", "appsodo")
        self.country = dict_app_country.get(self.language, "US")
