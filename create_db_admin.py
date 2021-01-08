# -*- encoding: utf-8 -*-

"""
@version: 1.00
@author: yaojiaqing
@contact: 24605071@qq.com
@site: http://www.yaojiaqing.com/
@software: PyCharm
@file: create_db_admin.py
@time: 2021/1/8 下午2:44
"""
from app import db
from manage import app
from app.model.models import  User,  Role
from flask_security import SQLAlchemyUserDatastore, Security
# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
db.create_all()
# 创建管理员
admin = user_datastore.create_user(email='admin@0993178.com', password='Ykxc201904')
# 创建普通用户角色和Admin角色
user_role = user_datastore.create_role(name='User', description='Generic user role')
admin_role = user_datastore.create_role(name='Admin', description='Admin user role')
# 为admin添加Admin角色(admin_role)
user_datastore.add_role_to_user(admin, admin_role)
db.session.commit()
