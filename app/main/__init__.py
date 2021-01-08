# -*- encoding: utf-8 -*-

"""
@version: 1.00
@author: yaojiaqing
@contact: 24605071@qq.com
@site: http://www.yaojiaqing.com/
@software: PyCharm
@file: __init__.py
@time: 2021/1/7 下午2:14
"""
from flask import Blueprint
main = Blueprint('main', __name__)

from . import views, errors