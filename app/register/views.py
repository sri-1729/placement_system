from . import register
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from .forms import RegisterForm

@register.route('/', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		userid = form.userId.data
		password = form.password.data
		cpassword = form.cpassword.data
		type_ = form.type_.data
		if password != cpassword:
			return render_template('reg_error.html')
		sql1 = f"SELECT userid FROM login where userid = '{userid}'"
		res = db.engine.execute(sql1).first()
		if not res:
			sql2 = f"INSERT INTO login(userid, password, type_) VALUES('{userid}', '{password}', '{type_}')"
			db.engine.execute(sql2)
			db.session.commit()
			return redirect(url_for('main.home'))
		else:
			return render_template('reg_error.html')
	return render_template('register.html', form = form)