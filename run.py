import os,sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from flask.ext.sqlalchemy import SQLAlchemy
 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/eason.db'
db = SQLAlchemy(app)
 
 
class Page(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    dis = db.Column(db.String())
    content=db.Column(db.Text)
    shu=db.Column(db.Integer)
    #times=db.Column(db.DateTime)
    #edit_time=db.Column(db.DateTime)
    ding=db.Column(db.Integer)
    imgurl=db.Column(db.Text)
    trees=db.Column(db.String(100))
    cid = db.Column(db.Integer, db.ForeignKey('think_class.id'))


class think_class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names=db.Column(db.String(50))
    xu=db.Column(db.Integer)
    dis=db.Column(db.String(20))
    trees=db.Column(db.String(60))
    url=db.Column(db.String(255))
   # IDtime=db.Column(db.DateTime)
    articles = db.relationship('Page', backref='clss',lazy='dynamic')
    cid=db.Column(db.Integer)

    def __repr__(self):
        return '<Class: %s>' % self.id
    


#db.create_all()
 

@app.route('/')
def index():
    dongtai=think_class.query.filter(think_class.cid==12).all()
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


@app.route('/content/<int:id>')
def content(id):
    content=Page.query.filter(Page.id==id).first()
    return render_template(
        'wenzhang.html',content=content
    )

@app.route('/lu/<int:id>/<int:status>')
def lu(id,status):
    left_nav=think_class.query.filter(think_class.cid==id).all()
    #print status
    position_two=think_class.query.filter(think_class.id==status).first()
    return render_template(
        'content.html',
        left_nav=left_nav,
        position_two=position_two
    )


if __name__ == '__main__':
    app.run(debug=True) 