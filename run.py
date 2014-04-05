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
    cid=db.Column(db.Integer)

    def __repr__(self):
        return str(self.title)

class Clss(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    names=db.Column(db.String(50))
    cid=db.Column(db.Integer)
    xu=db.Column(db.Integer)
    dis=db.Column(db.String(20))
    trees=db.Column(db.String(60))
    url=db.Column(db.String(255))
    IDtime=db.Column(db.DateTime)
#db.create_all()
 

@app.route('/')
def people():
    query_user = Page.query.filter(Page.cid==79).all()
    return query_user
    #return render_template('index.html')

 
if __name__ == '__main__':
    app.run(debug=True) 