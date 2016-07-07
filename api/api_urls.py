#!/usr/bin/env python3
# _*_coding:utf-8_*_
from api.handler.questionHandler import QuestionApiHandler

api_urls = [
    (r"/api/question", QuestionApiHandler),

]
