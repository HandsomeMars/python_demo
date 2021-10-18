#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Created by zyj at 2021/10/15.
    Description:
    Changelog: all notable changes to this file will be documented
"""

# -*- coding: utf-8 -*-
# !/usr/bin/env python

import gettext
import os

# 翻译资源名
APP_NAME = "resource"
# 翻译文件位置
LOCALE_DIR = os.path.abspath("./locale")
# 将域APP_NAME与LOCALE_DIR目录绑定，
# 这样gettext函数会在LOCALE_DIR目录下搜索对应语言的二进制APP_NAME.mo文件
gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
# 声明使用现在的域，可以使用多个域，便可以为同一种语言提供多套翻译，
# 本程序只使用了一个域
gettext.textdomain(APP_NAME)

# 使用对应语言翻译 （此步骤可以通过手动进行）
_= gettext.translation(APP_NAME, LOCALE_DIR, ["zh-CN", "en-US"]).gettext
# _ = gettext.gettext
# gettext.translation(APP_NAME, LOCALE_DIR, ["zh-CN", "en-US"]).gettext

if __name__ == "__main__":
    print (_("hello world"))

# APP_NAME = "resource"
# LOCALE_DIR = os.path.abspath("./locale")
# gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
# # 这条语句会将_()函数自动放到python的内置命名空间中
# _ = gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
# # 获取简体中文翻译类的实例
# lang_zh_CN = gettext.translation(APP_NAME, LOCALE_DIR, ["zh-CN"])
# # 获取英文翻译类的实例
# lang_en = gettext.translation(APP_NAME, LOCALE_DIR, ["en-US"])
#
#
# if __name__ == "__main__":
#     # 安装中文
#     lang_zh_CN.install()
#     _=lang_zh_CN.gettext
#     print(_("hello world"))
#     # 安装英文（程序中实时切换回英文）
#     lang_en.install()
#     _ = lang_en.gettext
#     print (_("hello world"))