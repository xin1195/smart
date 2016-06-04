#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/5/25
from tornado.ioloop import IOLoop

from setting import client

db = client.test_database


# 插入一个值到mongodb
# def my_callback(result, error):
#     print('result %s' % repr(result))
#     IOLoop.instance().stop()
#
# document = {'key1': 'value1'}
# db.test_collection.insert(document, callback=my_callback)
# IOLoop.instance().start()

# 循环插入一个值到mongodb
i = 0
def do_insert(result, error):
    global i
    if error:
        raise error
    i += 1
    if i < 2000:
        db.test_collection.insert({'i': i}, callback=do_insert)
    else:
        IOLoop.instance().stop()
# Start
db.test_collection.insert({'i': i}, callback=do_insert)
IOLoop.instance().start()

# 异步循环插入一个值到mongodb
# @gen.coroutine
# def do_insert():
#     for i in range(2000):
#         future = db.test_collection.insert({'i': i})
#         result = yield future
# IOLoop.current().run_sync(do_insert)

# async def do_insert():
#     for i in range(2000):
#         result = await db.test_collection.insert({'i': i})
# IOLoop.current().run_sync(do_insert)

# MotorCollection.find_one
# @gen.coroutine
# def do_find_one():
#     document = yield db.test_collection.find_one({'i': {'$lt': 1}})
#     pprint.pprint(document)
# IOLoop.current().run_sync(do_find_one)



# MotorCollection.find
# @gen.coroutine
# def do_find():
#     cursor = db.test_collection.find({'i': {'$lt': 5}}).sort('i')
#     for document in (yield cursor.to_list(length=100)):
#         pprint.pprint(document)
# IOLoop.current().run_sync(do_find)

# To get one document at a time with fetch_next and MotorCursor.next_object:
# @gen.coroutine
# def do_find():
#     cursor = db.test_collection.find({'i': {'$lt': 5}})
#     while (yield cursor.fetch_next):
#         document = cursor.next_object()
#         pprint.pprint(document)
# IOLoop.current().run_sync(do_find)


# You can apply a sort, limit, or skip to a query before you begin iterating:
# @gen.coroutine
# def do_find():
#     c = db.test_collection
#     cursor = c.find({'i': {'$lt': 5}})
#     # Modify the query before iterating
#     cursor.sort('i', -1).limit(2).skip(2)
#     while (yield cursor.fetch_next):
#         document = cursor.next_object()
#         pprint.pprint(document)
# IOLoop.current().run_sync(do_find)


# async for
# In a native coroutine defined with async def, replace the while-loop with async for:
# async def do_find():
#     c = db.test_collection
#     async for document in c.find({'i': {'$lt': 2}}):
#         pprint.pprint(document)
# IOLoop.current().run_sync(do_find)


# Use MotorCursor.count to determine the number of documents in a collection, or the number of documents that match a query:
# @gen.coroutine
# def do_count():
#     n = yield db.test_collection.find().count()
#     print('%s documents in collection' % n)
#     n = yield db.test_collection.find({'i': {'$gt': 1000}}).count()
#     print('%s documents where i > 1000' % n)
# IOLoop.current().run_sync(do_count)


# Updating Documents
# MotorCollection.update changes documents. It requires two parameters: a query that specifies which documents to update, and an update document.
# The query follows the same syntax as for find() or find_one(). The update document has two modes: it can replace the whole document, or it can update some fields of a document. To replace a document:
# @gen.coroutine
# def do_replace():
#     coll = db.test_collection
#     old_document = yield coll.find_one({'i': 50})
#     print('found document: %s' % pprint.pformat(old_document))
#     _id = old_document['_id']
#     result = yield coll.update({'_id': _id}, {'key': 'value'})
#     print('replaced %s document' % result['n'])
#     new_document = yield coll.find_one({'_id': _id})
#     print('document is now %s' % pprint.pformat(new_document))
# IOLoop.current().run_sync(do_replace)


# You can see that update() replaced everything in the old document except its _id with the new document.
# Use MongoDB’s modifier operators to update part of a document and leave the rest intact. We’ll find the document whose “i” is 51 and use the $set operator to set “key” to “value”:
# @gen.coroutine
# def do_update():
#     coll = db.test_collection
#     result = yield coll.update({'i': 53}, {'$set': {'key': 'value'}}, multi=True)
#     print('updated %s document' % result['n'])
#     new_document = yield coll.find_one({'i': 53})
#     print('document is now %s' % pprint.pformat(new_document))
# IOLoop.current().run_sync(do_update)

# “key” is set to “value” and “i” is still 51.
# By default update() only affects the first document it finds, you can update all of them with the multi flag:
# yield coll.update({'i': {'$gt': 100}}, {'$set': {'key': 'value'}}, multi=True)


# Saving Documents
# MotorCollection.save is a convenience method provided to insert a new document or update an existing one. If the dict passed to save() has an "_id" key then Motor performs an update() (upsert) operation and any existing document with that "_id" is overwritten. Otherwise Motor performs an insert().
# @gen.coroutine
# def do_save():
#     coll = db.test_collection
#     doc = {'key': 'value'}
#     yield coll.save(doc)
#     print('document _id: %s' % repr(doc['_id']))
#     doc['other_key'] = 'other_value'
#     yield coll.save(doc)
#     yield coll.remove(doc)
# IOLoop.current().run_sync(do_save)


# Removing Documents
# MotorCollection.remove takes a query with the same syntax as MotorCollection.find. remove() immediately removes all matching documents.
# @gen.coroutine
# def do_remove():
#     coll = db.test_collection
#     n = yield coll.count()
#     print('%s documents before calling remove()' % n)
#     result = yield db.test_collection.remove({'i': {'$gte': 1000}})
#     print('%s documents after' % (yield coll.count()))
# IOLoop.current().run_sync(do_remove)


# Commands
# Besides the “CRUD” operations–insert, update, remove, and find–all other operations on MongoDB are commands. Run them using the MotorDatabase.command method on MotorDatabase:
# from bson import SON
# @gen.coroutine
# def use_count_command():
#     response = yield db.command(SON([("count", "test_collection")]))
#     print('response: %s' % pprint.pformat(response))
# IOLoop.current().run_sync(use_count_command)

# Since the order of command parameters matters, don’t use a Python dict to pass the command’s parameters. Instead, make a habit of using bson.SON, from the bson module included with PyMongo:
# yield db.command(SON([("distinct", "test_collection"), ("key", "my_key"]))


























































