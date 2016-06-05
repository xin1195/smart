#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/6/2
import time
from tornado import gen

from tornado_json import schema
from api.handler.baseApiHandler import BaseApiHandler


class ApiAppGenreHandler(BaseApiHandler):
    @schema.validate()
    @gen.coroutine
    def get(self):
        data_list = []
        games_items = []
        apps_items = []
        games_genre_name = ""
        apps_genre_name = ""
        cursor = self.db.apple_genre.find({'parentId': {'$in': [6014, 36]}}, {"_id": 0})
        while (yield cursor.fetch_next):
            apple_genre = cursor.next_object()
            apple_genre_dict = {"apple_genre": apple_genre.get(self.country.upper()),
                                "genreId": apple_genre.get("genreId"),
                                "icon2_file": "http://pic.api.vshare.com/" + str(apple_genre.get("icon2_file")),
                                "introduce": ""
                                }
            if apple_genre.get("parentId", 0) == 6014 and apple_genre.get("genreId") != 6014:
                games_items.append(apple_genre_dict)
            elif apple_genre.get("parentId", 0) == 6014 and apple_genre.get("genreId") == 6014:
                games_genre_name = apple_genre.get(self.country.upper())
            elif apple_genre.get("parentId", 0) == 36 and apple_genre.get("genreId") != 6014:
                apps_items.append(apple_genre_dict)
            elif apple_genre.get("parentId", 0) == 36 and apple_genre.get("genreId") == 36:
                apps_genre_name = apple_genre.get(self.country.upper())
        games_dict = {"genreId": 6014, "genreName": games_genre_name, "items": games_items}
        apps_dict = {"genreId": 36, "genreName": apps_genre_name, "items": apps_items}
        data_list.append(games_dict)
        data_list.append(apps_dict)
        use_time = {"time": time.time() - self.start_time}
        data_list.append(use_time)
        return data_list
