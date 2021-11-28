from . import role
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db

# @role.route('/create')
# @login_required
# def role_create():

# 	if form.validate_on_submit():
# 		title = form.title.data
# 		jd_link = form.jd_link.data
# 		ctc = form.ctc.data
# 		last_date = form.last_date.data
# 		sql1 = f"INSERT INTO role(company_id, title, jd_link, ctc, last_date) VALUES('{session['user']['userid']}', '{title}', '{jd_link}', '{ctc}', last_date)"
# 		db.engine.execute(sql1)
# 		db.session.commit()
# 		return redirect(url_for('role.schedule_create', role_id = ))
# 	return render_template('role_create.html', form = form)

# @role.route('/schedule')
# @login_required
# def schedule_create():
# 	if form.validate_on_submit():
# 		ppt_date = form.ppt_date.data
# 		test_date = form.test_date.data
# 		interview_date = form.interview_date.data
# 		ppt_link = form.ppt_link.data
# 		test_link = form.test_link.data
# 		interview_link = form.interview_link.data
# 		sql1 = f"INSERT INTO schedule(ppt_date, test_date, interview_date, ppt_link, test_link, interview_link) VALUES({ppt_date}, {test_date}, {interview_date}, '{ppt_link}', '{test_link}', '{interview_link}')"
# 		db.engine.execute(sql1)
# 		db.session.commit()
# 		return redirect(url_for('main.home'))
# 	return render_template('schedule_create.html', form = form)



