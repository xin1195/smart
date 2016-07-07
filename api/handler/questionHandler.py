#!/usr/bin/env python3
# Created by Administrator on 2016/7/7.
from tornado import gen

from api.handler.baseHandler import BaseApiHandler
from setting import g_redis_time_30m


class QuestionApiHandler(BaseApiHandler):
    """
        问题类：用于查询问题
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.results = []
        self.question = self.get_argument("q", "")

    @gen.coroutine
    def get(self):
        # 判断redis 是否存在
        self.results = yield self.get_results_redis()
        if not self.results:
            if self.question:
                where = {"question": self.question}
                show = {"_id": 0}
                info_question = yield self.db.info_question_cn.find_one(where, show)
                if info_question:
                    answer = info_question.get("answer")
                else:
                    answer = "对不起，你提的问题我不知道！"
                self.results.append(answer)
                # 加入redis
                data_dict = {"results": self.results}
                yield gen.Task(self.redis_db.set, self.request.uri, data_dict, g_redis_time_30m)
            else:
                self.results.append("question 参数为空")
        return self.change_to_jsonp(self.results)
