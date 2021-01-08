# -*- encoding: utf-8 -*-

"""
@version: 1.00
@author: yaojiaqing
@contact: 24605071@qq.com
@site: http://www.yaojiaqing.com/
@software: PyCharm
@file: manage.py
@time: 2021/1/7 下午2:02
"""

from app import create_app, db
from app.model.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_babelex import Babel
from flask_admin import Admin, form
from flask_security import SQLAlchemyUserDatastore, Security
from flask_ckeditor import  CKEditor

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
ckeditor = CKEditor(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

admin = Admin(app, name='粤客小厨后台管理系统', base_template='my_master.html', template_mode='bootstrap4')


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()