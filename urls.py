#!/usr/bin/python3
# _*_coding:utf-8_*_
from admin.admin_urls import admin_urls
from api.api_urls import api_urls
from home.home_urls import home_urls

urls = []
urls.extend(admin_urls)
urls.extend(api_urls)
urls.extend(home_urls)
