import sqlite3
from flask import Flask,session,g,redirect,url_for,abort,render_template,flash
DATABASE='tmp/eason.db'
DEBUG=True
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD='123'