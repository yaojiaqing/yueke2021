# -*- encoding: utf-8 -*-

"""
@version: 1.00
@author: yaojiaqing
@contact: 24605071@qq.com
@site: http://www.yaojiaqing.com/
@software: PyCharm
@file: models.py
@time: 2021/1/7 下午4:27
"""
from app import db
from flask_security import RoleMixin, UserMixin, current_user
from flask import request, url_for, redirect, abort
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import text

# 定义模型
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    wx_openid = db.Column(db.String(64))
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(100))
    nikename = db.Column(db.String(100))
    mobile = db.Column(db.String(11))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Create customized model view class
class MyModelView(ModelView):

    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
        )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name

class Menutype(db.Model):

    #菜品类型
    __tablename__ = "menutypes"

    menu_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_type_name = db.Column(db.String(60), unique=True,nullable=False)
    menu_type_desc = db.Column(db.Text(100))
    menu_type_type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Menutype %r>' % self.menu_type_name

class MVmenutypes(MyModelView):

    column_labels = {
        'menu_type_id':'菜品类型编码',
        'menu_type_name':'菜品类型名称',
        'menu_type_desc':'菜品类型描述',
        'menu_type_type':'备注',
        'images':'产品图片',
    }
    column_list = ('menu_type_id', 'menu_type_name', 'menu_type_desc', 'menu_type_type')
    def __init__(self, session, **kwargs):
        super(MVmenutypes, self).__init__(Menutype, session, **kwargs)

class Menu(db.Model):

    #菜品
    __tablename__ = "menus"

    menu_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_name = db.Column(db.String(80), unique=True, nullable=False)
    menu_desc = db.Column(db.Text(200))
    create_datetime = db.Column(db.TIMESTAMP(timezone=False), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    type_id = db.Column(db.Integer, db.ForeignKey('menutypes.menu_type_id')) #菜品分类
    is_bossintro = db.Column(db.Boolean, default=False, server_default=text('0')) #是否老板推荐
    is_new = db.Column(db.Boolean, default=False, server_default=text('0')) #是否新品
    is_active = db.Column(db.Boolean, default=False, server_default=text('0')) #是否正在销售菜品
    price_now = db.Column(db.Float,nullable=False, default=28) #菜品单价
    menu_unit = db.Column(db.String(10), default="份") #单位：盘，客，例等
    images = db.relationship('Image', backref='menus') #菜品配图
    image_id = db.Column(db.ForeignKey(Image.id)) #主配图

    type_name = db.relationship('Menutype', backref=db.backref('menutypes'), lazy='select')

    def __repr__(self):
        return '<Menu %r>' % self.menu_name

class MVmenu(MyModelView):

    column_labels = {
        'menu_id':'菜品编码',
        'menu_name':'菜品名称',
        'menu_desc':'菜品描述',
        'type_id':'菜品类型',
        'is_bossintro':'老板推荐',
        'is_new':'是否新品',
        'is_active':'是否有售',
        'price_now':'目前单价',
        'menu_unit':'装盘单位',
        'image_id':'菜品主图',
        'images':'菜品所有配图',
        'type_name':'菜品类型组合',
    }
    column_list = ('menu_id','menu_name', 'menu_desc', 'type_id', 'is_bossintro', 'is_new', 'is_active', 'price_now', 'menu_unit', 'image_id', 'images', 'type_name')

    def __init__(self, session, **kwargs):
        super(MVmenu, self).__init__(Menu, session, **kwargs)