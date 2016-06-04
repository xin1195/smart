#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/5/25
import pprint
from asyncio import coroutine
import asyncio
from setting import client

# Creating a Client
# client = motor.motor_asyncio.AsyncIOMotorClient()
# client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
# Getting a Database


db = client.test_database
# db = client['test_database']


# Inserting a Document
# As in PyMongo, Motor represents MongoDB documents with Python dictionaries. To store a document in MongoDB, call AsyncIOMotorCollection.insert in a yield from statement:
# @coroutine
# def do_insert():
#     document = {'key': 'value'}
#     result = yield from db.test_collection.insert(document)
#     print('result %s' % repr(result))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_insert())


# Using native coroutines
# Starting in Python 3.5, you can define a native coroutine with async def instead of the gen.coroutine decorator. Within a native coroutine, wait for an async operation with await instead of yield:
# async def do_insert():
#     for i in range(2000):
#         result = await db.test_collection.insert({'i': i})
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_insert())


# Getting a Single Document With find_one
# @coroutine
# def do_find_one():
#     document = yield from db.test_collection.find_one({'i': {'$lt': 1}})
#     pprint.pprint(document)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_find_one())


# Querying for More Than One Document
@coroutine
def do_find():
    cursor = db.test_collection.find({'i': {'$lt': 5}}).sort('i')
    for document in (yield from cursor.to_list(length=100)):
        pprint.pprint(document)
loop = asyncio.get_event_loop()
loop.run_until_complete(do_find())


# To get one document at a time with fetch_next and AsyncIOMotorCursor.next_object:
# @coroutine
# def do_find():
#     cursor = db.test_collection.find({'i': {'$lt': 5}})
#     while (yield from cursor.fetch_next):
#         document = cursor.next_object()
#         pprint.pprint(document)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_find())


# You can apply a sort, limit, or skip to a query before you begin iterating:
# @coroutine
# def do_find():
#     cursor = db.test_collection.find({'i': {'$lt': 5}})
#     # Modify the query before iterating
#     cursor.sort('i', -1).limit(2).skip(2)
#     while (yield from cursor.fetch_next):
#         document = cursor.next_object()
#         pprint.pprint(document)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_find())


# async for
# async def do_find():
#     c = db.test_collection
#     async for document in c.find({'i': {'$lt': 2}}):
#         pprint.pprint(document)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_find())


# Counting Documents
# @coroutine
# def do_count():
#     n = yield from db.test_collection.find().count()
#     print('%s documents in collection' % n)
#     n = yield from db.test_collection.find({'i': {'$gt': 1000}}).count()
#     print('%s documents where i > 1000' % n)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_count())


# Updating Documents
# @coroutine
# def do_replace():
#     coll = db.test_collection
#     old_document = yield from coll.find_one({'i': 50})
#     print('found document: %s' % pprint.pformat(old_document))
#     _id = old_document['_id']
#     result = yield from coll.update({'_id': _id}, {'key': 'value'})
#     print('replaced %s document' % result['n'])
#     new_document = yield from coll.find_one({'_id': _id})
#     print('document is now %s' % pprint.pformat(new_document))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_replace())


# Use MongoDB’s modifier operators to update part of a document and leave the rest intact. We’ll find the document whose “i” is 51 and use the $set operator to set “key” to “value”:
# @coroutine
# def do_update():
#     coll = db.test_collection
#     result = yield from coll.update({'i': 51}, {'$set': {'key': 'value'}})
#     print('updated %s document' % result['n'])
#     new_document = yield from coll.find_one({'i': 51})
#     print('document is now %s' % pprint.pformat(new_document))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_update())


# Saving Documents
# @coroutine
# def do_save():
#     coll = db.test_collection
#     doc = {'key': 'value'}
#     yield from coll.save(doc)
#     print('document _id: %s' % repr(doc['_id']))
#     doc['other_key'] = 'other_value'
#     yield from coll.save(doc)
#     yield from coll.remove(doc)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_save())


# Removing Documents
# @coroutine
# def do_remove():
#     coll = db.test_collection
#     n = yield from coll.count()
#     print('%s documents before calling remove()' % n)
#     result = yield from db.test_collection.remove({'i': {'$gte': 1000}})
#     print('%s documents after' % (yield from coll.count()))
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_remove())


# Commands
# from bson import SON
# @coroutine
# def use_count_command():
#     response = yield from db.command(SON([("count", "test_collection")]))
#     print('response: %s' % pprint.pformat(response))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(use_count_command())










































































































































