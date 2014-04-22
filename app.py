from flask import Flask,g,render_template,request


from flask_wtf.csrf import CsrfProtect

from project.master.view import master_app
from project.admin_master.view import admin_app
from project.extension.database import db,setup_database
from project.extension.login_manager import setup_login_manager


csrf = CsrfProtect()
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='fuckoff'
    app.config['CSRF_ENABLED ']=False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/eason.db'
    app.register_blueprint(master_app)
    app.register_blueprint(admin_app)
    setup_database(app)
    setup_login_manager(app)
    csrf.init_app(app)
    return app