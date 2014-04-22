from flask.ext.sqlalchemy import SQLAlchemy
 
from project.extension.database import db


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
    children_id = db.Column(db.Integer, db.ForeignKey('think_class.id'))
    children=db.relationship('think_class',backref='parent', remote_side='think_class.id')
   # IDtime=db.Column(db.DateTime)
    articles = db.relationship('Page', backref='clss',lazy='dynamic')
    cid=db.Column(db.Integer)

    @property
    def all_articles(self):
        articles = []
        for child in self.children:
            articles = articles + child.articles
        return articles

    def __repr__(self):
        return '<Class: %s>' % self.id
    

class User(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20))
    password=db.Column(db.String(20))


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)