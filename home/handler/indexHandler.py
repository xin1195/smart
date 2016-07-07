#!/usr/bin/env python3

import tornado.httpclient
import tornado.web
from tornado import gen

from home.handler.baseHandler import BaseHandler


class HomeIndexHandler(BaseHandler):
    def get(self):
        self.render("home/index.html")


class HomeIndex2Handler(BaseHandler):
    def get(self):
        self.render("home/index2.html")


class HomeIndex3Handler(BaseHandler):
    def get(self):
        self.render("home/index3.html")


class HomeIndex4Handler(BaseHandler):
    def get(self):
        self.render("home/index4.html")

    @gen.coroutine
    def post(self, *args, **kwargs):
        query = self.get_argument("q", "")
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch, "http://localhost:8000/api/question?q=%s" % query)
        body = eval(response.body)
        time = body.get("time", 0)
        results = body.get("results", "")
        self.render("home/search_response.html", time=time, results=results)

