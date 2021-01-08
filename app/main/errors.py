# -*- encoding: utf-8 -*-

"""
@version: 1.00
@author: yaojiaqing
@contact: 24605071@qq.com
@site: http://www.yaojiaqing.com/
@software: PyCharm
@file: errors.py
@time: 2021/1/7 下午3:33
"""
from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
