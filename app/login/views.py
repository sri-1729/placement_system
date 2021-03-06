from . import login
from flask import render_template, redirect, session, url_for,jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from .forms import LoginForm
from ..models import Login

#To validate the Login Information provided and start session by the corresponding user
@login.route('/login', methods = ['POST', 'GET'])
def logIn():
	form = LoginForm()
	if form.validate_on_submit():
		#query the table to get the user
		sql1 = f"SELECT * FROM login WHERE userid = '{form.userId.data}';"
		user = db.engine.execute(sql1).first()
		if(user==None):
			msg='Invalid Userid'
			
			return render_template('login.html', form = form,msg=msg)
		user=dict(user)
		#for authentication purposes only
		user_auth = Login.query.get(form.userId.data)
		
		#if user is found
		if user:
			#check if password is matching
			if user['password'] == form.password.data:
				session['user'] = user
				user_auth.auth = True
				login_user(user_auth)
				return redirect(url_for('main.home'))
		#if user is not there or password is incorrect
		msg='Invalid Password'
		return render_template('login.html', form = form,msg=msg)
	msg=''
	return render_template('login.html', form = form,msg=msg)

#To logout the user from the session
@login.route("/logout", methods=["GET"])
@login_required
def logout():
	"""Logout the current user."""
	user = current_user
	user.auth = False
	session.pop('user')
	logout_user()
	return redirect(url_for('main.home'))
