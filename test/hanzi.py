#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time
import traceback

import pymongo

# text = """吖】ā［吖嗪］（āqín）名有机化合物的一类，呈环状结构，含有一个或几个氮原子，如吡啶、哒嗪、嘧啶等。［英azine］
#
# 【阿】ā〈方〉前缀。①用在排行、小名或姓的前面，有亲昵的意味：～大｜～宝｜～唐。②用在某些亲属名称的前面：～婆｜～爹｜～哥。
# 另见2页•ɑ“啊”；354页ē。
#
# 【阿鼻地狱】ābídìyù佛教指最深层的地狱，是犯了重罪的人死后灵魂永远受苦的地方。"""

# file = open('zidian_c.txt', "r", encoding="utf-8")
# try:
#     word_list = []
#     all_the_text = file.read()
#     text_list = all_the_text.split("【")
#     for text in text_list:
#         temp_list = text.split("】")
#         word_list.append({"name": temp_list[0], "description": temp_list[1]})
#     print(word_list)
# finally:
#     file.close()

# for text in texts:
# if "\u4E00" < text < "\u9FBF":
# if text == "\u3010":
#     print(text)
# if text == "\u3011":
#     print(text)
# if "\u0000" <= text <= "\u024F":
#     print(text)


# text_list = text.split("【")
# for text in text_list:
#     text_list_list = text.split("】")
#     print(text_list_list)
from setting import logger

conn = pymongo.Connection(host='112.74.204.250', port=27017)
db = conn.smartSearch


def get_word_list(file_name):
    w_list = []
    f = open(file_name, "r", encoding="utf-8")
    try:
        all_text = f.read()
        t_list = all_text.split("【")
        for tex in t_list:
            tex = tex.replace("\n", "")
            if tex and tex.find("】"):
                tem_list = tex.split("】")
                if tem_list[0] and tem_list[1]:
                    w_list.append({"name": tem_list[0], "description": tem_list[1]})
        return w_list
    except:
        logger.error(traceback.format_exc())
        return w_list
    finally:
        f.close()


def update_to_mongo(w_list):
    for w_dict in w_list:
        print(w_dict)
        db.info_word.update({"name": w_dict.get("name", "")}, w_dict, upsert=True)


def main():
    w_list = get_word_list("zidian.txt")
    # print(w_list)
    update_to_mongo(w_list)
    print("更新完成")


if __name__ == "__main__":
    main()
