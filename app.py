from flask import Flask, render_template, requestfrom flask.ext.sqlalchemy import SQLAlchemy  app = Flask(__name__)app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.sqlite'db = SQLAlchemy(app)  class People(db.Model):     id = db.Column(db.Integer, primary_key=True)    username = db.Column(db.String(10))    pwd = db.Column(db.String(64))  db.create_all()  @app.route('/')def hello_world():    return render_template('base.html')  @app.route('/test')def test():    hello = request.args.get('hello')    world = request.args.get('world')    return render_template(        'index.html', hello=hello, world=world    )  @app.route('/form', methods=['POST'])def form():    username = request.form.get('username')    pwd = request.form.get('pwd')    people = People()    people.username = username    people.pwd = pwd    db.session.add(people)    db.session.commit()    return 'username = %s <br /> password = %s' % (username, pwd)  @app.route('/people/<username>')def people(username):    query_user = People.query.filter(People.username==username).first()    return 'people: %s' % query_user.pwd  @app.route('/update/<username>')def update(username):    new_pwd = request.args.get('new_pwd')    query_user = People.query.filter(People.username==username).first()    query_user.pwd = new_pwd    db.session.add(query_user)    db.session.commit()    return 'update: %s' % query_user.pwd  @app.route('/delete/<username>')def delete(username):    query_user = People.query.filter(People.username==username).first()    db.session.delete(query_user)    db.session.commit()    return 'deleted'  if __name__ == '__main__':    app.run(debug=True)