#!/usr/bin/env python3


import pymongo

MONGOURL = 'mongodb://112.74.204.250:27017'
db = pymongo.MongoClient(MONGOURL).smartSearch


def xiao_tian_answer(question=""):
    if question:
        # where = {"question": {"$regex": question}}
        where = {"question": question}
        show = {"_id": 0}
        info_question = db.info_question_cn.find_one(where, show)
        print("info_question", info_question)
        if info_question:
            answer = info_question.get("answer")
        else:
            answer = "对不起，你提的问题我不知道！"
        return answer
