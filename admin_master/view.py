
import os,sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask import Blueprint

from project.model.account import User, Page,think_class
from project.extension.database import db
from project.forms.account import LoginForm,addForm
from project.extension.pagination import Pagination

admin_app = Blueprint('admin_master', __name__,)
per_page=10

@admin_app.route('/admin/<int:page>')
def admin(page=1):
    pagination=Page.query.paginate(page,per_page,False)
    object_list = pagination.items
    main_nav=think_class.query.all()
    return render_template(
        'admin/admin.html',pagination=pagination,object_list=object_list,main_nav=main_nav)

@admin_app.route('/feilei/id/<int:id>/page/<int:page>')
def fenlei(id,page):
    #content=think_class.query.filter(think_class.cid==id).all()
    #eason=content[0].articles
    #pagination=eason.paginate(page,per_page,False)
    
    content=think_class.query.filter(think_class.id==14).first()
    #print dir(content)
    for u in content.children:
        print u.names
    return 'sdfsdf'
    pagination=content.articles.paginate(page,per_page,False)
    object_list = pagination.items
    main_nav=think_class.query.all()
    return render_template(
        'admin/admin.html',pagination=pagination,object_list=object_list,main_nav=main_nav)


@admin_app.route('/add')
def add():
    form=addForm()
    if form.validate_on_submit():
        print 'success'
    return render_template('admin/add.html',form=form)

@admin_app.route('/save_add', methods = ['GET', 'POST'])
def save_tianjia():
    form=addForm()
    if form.validate_on_submit():
        print form.title.data
        return 'sdfsdfs dd'
    page=Page()
    print request.form.get('title')
    return 'sdfasd'