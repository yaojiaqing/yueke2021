# -*- encoding: utf-8 -*-

"""
@version: 1.00
@author: yaojiaqing
@contact: 24605071@qq.com
@site: http://www.yaojiaqing.com/
@software: PyCharm
@file: views.py
@time: 2021/1/7 下午2:20
"""

from flask import render_template
from . import main

@main.route("/")
def index():
    return render_template('main/index.html')

@main.route("/favicon.ico")
def favicon():
    return main.send_static_file("main/favicon.ico")