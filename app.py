from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# ENGLISH

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('about.html')

    



