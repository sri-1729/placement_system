from . import role
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from .forms import RoleForm, ScheduleForm

@role.route('/create', methods = ['GET', 'POST'])
@login_required
def role_create():
	form = RoleForm()
	if form.validate_on_submit():
		title = form.title.data
		jd_link = form.jd_link.data
		ctc = form.ctc.data
		last_date = form.last_date.data
		sql1 = f"INSERT INTO role(company_id, title, jd_link, ctc, last_date) VALUES('{session['user']['userid']}', '{title}', '{jd_link}', '{ctc}', '{last_date}') RETURNING role_id" 
		role_id = db.engine.execute(sql1).first()
		db.session.commit()
		return redirect(url_for('role.schedule_create', role_id = role_id))
	return render_template('role_create.html', form = form)

@role.route('/schedule/<string:role_id>', methods = ['GET', 'POST'])
@login_required
def schedule_create(role_id):
	form = ScheduleForm()
	if form.validate_on_submit():
		ppt_date = form.ppt_date.data
		test_date = form.test_date.data
		interview_date = form.interview_date.data
		ppt_link = form.ppt_link.data
		test_link = form.test_link.data
		interview_link = form.interview_link.data
		role_id = int(role_id[1])
		sql1 = f"INSERT INTO schedule(ppt_date, test_date, interview_date, ppt_link, test_link, interview_link) VALUES('{ppt_date}', '{test_date}', '{interview_date}', '{ppt_link}', '{test_link}', '{interview_link}') RETURNING schedule_id"
		schedule_id=db.engine.execute(sql1).first()['schedule_id']
		db.session.commit()
		sql2 = f"UPDATE role SET schedule_id = {schedule_id} WHERE role_id={role_id}"
		db.engine.execute(sql2)
		db.session.commit()
		return redirect(url_for('main.home'))
	return render_template('schedule_create.html', form = form)



