from . import role
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from .forms import RolesEligibilityForm,RoleForm, ScheduleForm

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
		z = int(role_id[1])
		sql1 = f"INSERT INTO schedule(ppt_date, test_date, interview_date, ppt_link, test_link, interview_link) VALUES('{ppt_date}', '{test_date}', '{interview_date}', '{ppt_link}', '{test_link}', '{interview_link}') RETURNING schedule_id"
		schedule_id=db.engine.execute(sql1).first()['schedule_id']
		db.session.commit()
		sql2 = f"UPDATE role SET schedule_id = {schedule_id} WHERE role_id={z}"
		db.engine.execute(sql2)
		db.session.commit()
		return redirect(url_for('role.roles_eligibilty',role_id=role_id))
		#return redirect(url_for('main.home'))
	return render_template('schedule_create.html', form = form)

@role.route('/roles/<string:role_id>', methods = ['GET', 'POST'])
@login_required
def roles_eligibilty(role_id):
	form = RolesEligibilityForm()
	z=int(role_id[1])
	sql = f"SELECT branch,cgpa FROM roles_eligibility WHERE role_id={z};"
	res = db.engine.execute(sql)
	print(z)
	if form.validate_on_submit():
		branch=form.branch.data
		cgpa=form.cgpa.data
		sql1 = f"INSERT INTO roles_eligibility(role_id,branch,cgpa) VALUES ('{z}','{branch}','{cgpa}')"
		db.engine.execute(sql1)
		db.session.commit()
		return redirect(url_for('role.roles_eligibilty',role_id=role_id))
	return render_template('roles_eligibility.html',form=form,res=res)
