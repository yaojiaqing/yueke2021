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
import os
import os.path as op

from app import create_app, db
from app.model.models import User, Role, Image, MyModelView
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_babelex import Babel
from flask_admin import Admin, form
from flask_security import SQLAlchemyUserDatastore, Security
from flask_admin import helpers as admin_helpers
from sqlalchemy.event import listens_for
from flask_ckeditor import  CKEditor
from flask import url_for
from jinja2 import Markup

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
ckeditor = CKEditor(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create directory for file fields to use
file_path = op.join(op.dirname(__file__), 'static/files')
try:
    os.mkdir(file_path)
except OSError:
    pass

class ImageView(MyModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename='files/'+form.thumbgen_filename(model.path)))

    column_formatters = {
        'path': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=file_path,
                                      thumbnail_size=(100, 100, True))
    }

class MVimage(ImageView):
    column_labels = {
        'id': '序号',
        'name': '图片说明',
        'path': '存放路径',
    }
    column_list = ('id','name','path')

    def __init__(self, session, **kwargs):
        super(MVimage, self).__init__(Image, session, **kwargs)

admin = Admin(app, name='粤客小厨后台管理系统', base_template='my_master.html', template_mode='bootstrap4')

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )

@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(file_path,
                              form.thumbgen_filename(target.path)))
        except OSError:
            pass

# 增加自定义过滤器，生成缩略图名称
@app.template_filter('thumb_filename')
def get_thumb_filename(tempfilename):
    (filename, extension) = os.path.splitext(tempfilename)
    return (filename+'_thumb'+extension)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()