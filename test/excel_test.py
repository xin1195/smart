#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 
# -*- coding: utf-8 -*-

import xlrd
import pymongo

conn = pymongo.Connection(host='112.74.204.250', port=27017)
db = conn.smartSearch


def open_excel(file='country.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='baojia.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file='baojia.xlsx', colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def updateToMongo_country(data_list):
    for data_dict in data_list:
        print(data_dict)
        db.bijia_country.update({"abbreviate": data_dict.get("abbreviate", "")}, data_dict, upsert=True)


def updateToMongo_price(data_list):
    for data_dict in data_list:
        print(data_dict)
        db.bijia_price.update({"line_code": data_dict.get("line_code", "")}, data_dict, upsert=True)

def main():
    data_list = excel_table_byindex()
    # updateToMongo_country(data_list)
    updateToMongo_price(data_list)

    # tables = excel_table_byname()
    # for row in tables:
    #     print(row)


if __name__ == "__main__":
    main()
