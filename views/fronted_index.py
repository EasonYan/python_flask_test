from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from app import app
 
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[0]) for row in cur.fetchall()]
    print entries
    return render_template('show_entries.html', entries=entries)