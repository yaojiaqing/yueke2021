# -*- encoding: utf-8 -*-

"""
@version: 1.00
@author: yaojiaqing
@contact: 24605071@qq.com
@site: http://www.yaojiaqing.com/
@software: PyCharm
@file: __init__.py
@time: 2021/1/7 下午12:53
"""
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from app.config import Config
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    bootstrap.init_app(app)

    app.config.from_object(Config)
    db.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app