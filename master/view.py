
import os,sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask import Blueprint
from flask.ext.login import login_user,logout_user,current_user

from project.model.account import User, Page,think_class
from project.extension.database import db
from project.forms.account import LoginForm

master_app = Blueprint('master', __name__,)

@master_app.route('/')
def index():
    dongtai=think_class.query.filter(think_class.cid==12).all()
    '''for u in dongtai:
        print u.title
       return 'sdfsdf'
    '''
    dongtaitongzhi=dongtai[0].articles.limit(8)
    dangjian=think_class.query.filter(think_class.cid==14).all()
    dangjiangongzuo=dangjian[0].articles.limit(8)
    ganbu=think_class.query.filter(think_class.cid==15).all()
    ganbugongzuo=ganbu[0].articles.limit(8)
    #flash('Document <strong>%s</strong> is missing.', 'error')
    return render_template(
        'index.html',
        dongtai=dongtai,
        dongtaitongzhi=dongtaitongzhi,
        dangjiangongzuo=dangjiangongzuo,
        ganbugongzuo=ganbugongzuo
    )



@master_app.route('/content/<int:id>')
def content(id):
    content=Page.query.filter(Page.id==id).first()
    return render_template(
        'wenzhang.html',content=content
    )

@master_app.route('/lu/<int:id>/<int:status>')
def lu(id,status):
    left_nav=think_class.query.filter(think_class.cid==id).all()
    #print status
    position_two=think_class.query.filter(think_class.id==status).first()
    return render_template(
        'content.html',
        left_nav=left_nav,
        position_two=position_two
    )

@master_app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        username=request.form['username'].strip()
        raw_passwd=request.form['password'].strip()
        user=User.query.filter(User.username==username).filter(User.password==raw_passwd).first()
        if user:
            print user.username
            return 'ssss'
        else:
            flash("you are a dog!!!")
            return redirect(url_for('master.login'))        
    return render_template('login.html',form=form)