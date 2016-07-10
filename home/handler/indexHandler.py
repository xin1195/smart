#!/usr/bin/env python3

import tornado.httpclient
import tornado.web
from tornado import gen

from home.handler.baseHandler import BaseHandler
from setting import domain


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
        response = yield tornado.gen.Task(client.fetch, domain + "api/word?q=%s" % query)
        body = eval(response.body)
        results = body.get("results", "")
        self.render("home/search_response.html", time=response.request_time, results=results)

