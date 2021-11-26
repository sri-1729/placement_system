from . import main
from flask import render_template
from .. import db

@main.route('/')
def home():
	db.create_all()
	return render_template('home.html')