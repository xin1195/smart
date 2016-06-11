#!/usr/bin/env python3
# _*_coding:utf-8_*_
from api.handler.appAppInfoHandler import ApiAppInfoHandler
from api.handler.appGenreHandler import ApiAppGenreHandler

api_urls = [
    (r"/api/app_genre/list", ApiAppGenreHandler),
    (r"/api/app/info", ApiAppInfoHandler),

]
