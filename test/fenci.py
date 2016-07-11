#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator on 2016/7/8.

import jieba

# text = "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。总会有一些功能是需要调用本地存档的。例如登录模块中，记住密码功能，会将密码信息存储在本地，以IE浏览器为例，在C:\Documents and Settings\（你的Windows用户名）\Application Data\Macromedia&nbsp;" \
#        "\Flash Player\#SharedObjects\（一些随机数字和字母）\ 文件夹下就可以看到存储密码的SOL文件，可以使用minerva工具查看，如下图所示，密码明文明文存储的，SOL文件是永久性保存的，除非手动清除，如果玩家在公共环境下登录，就会有盗号威胁。来自http://www.baidu.com/及http：、www.baidu...com"
text = "我来到北京清华大学"
seg_list = jieba.cut(text, cut_all=True)
print("Full Mode:", ' '.join(seg_list))

seg_list = jieba.cut(text)
print("Default Mode:", ' '.join(seg_list))
