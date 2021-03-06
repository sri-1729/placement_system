from . import main
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import render_template, redirect, session, url_for
from .. import db

#The Home Page in 4 instances, NO user or Company or TnP Admin or STudent
@main.route('/')
def home():
	db.create_all()
	msg='True'
	if 'user' in session :
		if session['user']['type_'] == 'company' :
			sql = f"SELECT * FROM COMPANY WHERE com_uid='{session['user']['userid']}'"
			res = db.engine.execute(sql).first()
			if not res or (not res['admin_id']):
				msg='False'
		if session['user']['type_'] == 'student' :
			sql = f"SELECT placement_status FROM profile WHERE stu_uid='{session['user']['userid']}'"
			res = db.engine.execute(sql).first()
			if res :
				if res['placement_status'] != 'Not Placed':
					msg='False'
	return render_template('home.html',msg=msg)
