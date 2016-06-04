#!/usr/bin/python3
# _*_coding:utf-8_*_
import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from setting import settings
from urls import urls

define("port", default=8000, help="run on the given port", type=int)

# 日志文件配置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='log/bcloud' + str(time.strftime("%Y%m%d%H%M%S")) + '.log',
                    filename='log/smartSearch.log',
                    filemode='w')

application = tornado.web.Application(
    handlers=urls,
    **settings
)


def main():
    # debug|info|warning|error|none 日志级别
    tornado.options.options.logging = "info"
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
