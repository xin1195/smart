#!/usr/bin/env python3
# _*_coding:utf-8_*_
from api.handler.questionHandler import QuestionApiHandler
from api.handler.wordHandler import WordApiHandler

api_urls = [
    (r"/api/question", QuestionApiHandler),
    (r"/api/word", WordApiHandler),

]
