#!/usr/bin/env python3

# UserSocket接口，用于浏览器通信
import json

import tornado.websocket

from home.handler.xiaoTianHandler import xiao_tian_answer
from setting import logger


def send_to_one_user(user_client, message):
    user_client.write_message(json.dumps(message))


def send_to_many_user(user_clients, message):
    for user_client in user_clients:
        user_client.write_message(json.dumps(message))


class UserSocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.user_client_map = {}

    def data_received(self, chunk):
        pass

    def send_to_all_user(self, message):
        for i in self.user_client_map:
            self.user_client_map[i].write_message(json.dumps(message))

    def open(self):
        self.write_message(json.dumps([{
            'cmd': 'open',
        }, {
            'form_user': 'system',
            'data': 'open:connect_success',
        }]))

    def on_close(self):
        pass

    def on_message(self, message):
        if message == 'heart':
            device_id = str(self.get_argument('device_id'))
            logger.info(device_id + ': 心跳连接正常')
        else:
            res = xiao_tian_answer(question=message)
            self.write_message({"message": res})
        logger.info({"message", message})

    def on_pong(self, data):
        logger.info({"on_pong", data})
