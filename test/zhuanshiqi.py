#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 


def my_auth(func):
    def inner():
        print("before")
        func()
        print("after")

    return inner


@my_auth
def f1():
    print("f1")


# f1()



def f2(arg):
    arg()


def func():
    print("func")


f2(func)