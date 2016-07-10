#!/usr/bin/env python3
# Created by Administrator on 2016/7/7.
from tornado import gen

from api.handler.baseHandler import BaseApiHandler
from setting import g_redis_time_30m


class WordApiHandler(BaseApiHandler):
    """
        文字类：用于查询问题
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.results = []
        self.word = self.get_argument("q", "")

    @gen.coroutine
    def get(self):
        # 判断redis 是否存在
        self.results = yield self.get_results_redis()
        if not self.results:
            if self.word:
                where = {"name": self.word}
                show = {"_id": 0}
                info_word = yield self.db.info_word_cn.find_one(where, show)
                if info_word:
                    description = info_word.get("description", "")
                else:
                    description = "对不起，你提的问题我不知道！"
                self.results.append(description)
                # 加入redis
                data_dict = {"results": self.results}
                yield gen.Task(self.redis_db.set, self.request.uri, data_dict, g_redis_time_30m)
            else:
                self.results.append("word 参数为空")
        return self.change_to_jsonp(self.results)
