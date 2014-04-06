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
def people():
    dongtai=think_class.query.filter(think_class.cid==12).all()
    dongtaitongzhi=dongtai[0].articles.limit(8)
    dangjian=think_class.query.filter(think_class.cid==14).all()
    dangjiangongzuo=dangjian[0].articles.limit(8)
    ganbu=think_class.query.filter(think_class.cid==15).all()
    ganbugongzuo=ganbu[0].articles.limit(8)
    #dongtai = think_class.query.filter(think_class.cid==12).first()
    #for u in dongtai.articles:
    #    print u.clss.id
    #print dongtai.articles.
    #dongtaitongzhi=dongtai.articles.limit(8)
    #print str(dir(dongtai))
    #for u in dongtai:
     #   print u.articles.all()
    #page=Page.query.filter(Page.cid==37).first()
    
    #return str(dir(dongtai))
    #for u in dongtai:
    #   print u.names
    #return dongtai.names
    #print str(dongtai)
    #print think_class.query.filter(think_class.cid==12)
    #print dongtai.articles.order_by(Page.id)
    #print dongtaitongzhi.names
    #page = Page.query.filter_by(id=122).first()
    #return 'sss'
    return render_template(
        'index.html',
        dongtai=dongtai,
        dongtaitongzhi=dongtaitongzhi,
        dangjiangongzuo=dangjiangongzuo,
        ganbugongzuo=ganbugongzuo
    )

 
if __name__ == '__main__':
    app.run(debug=True) 