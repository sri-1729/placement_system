from . import role
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from .forms import RolesEligibilityForm,RoleForm
from ..helper import strToInt, extract_date_httpFormat
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, DateField


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
	#sql query for getting range of dates available
	sql0 = f"SELECT * FROM available_dates WHERE company_id = '{session['user']['userid']}'"
	dates = db.engine.execute(sql0)
	ppt_date_from, ppt_date_to  = None, None
	test_date_from, test_date_to = None, None
	interview_date_from, interview_date_to = None, None

	for date in dates:
		each_date = dict(date)
		if(each_date['d_id'] == 'ppt_date'):
			ppt_date_from = extract_date_httpFormat(each_date['from'])
			ppt_date_to = extract_date_httpFormat(each_date['to'])
		elif(ppt_date['d_id'] == 'test_date'):
			test_date_from = extract_date_httpFormat(each_date['from'])
			test_date_to = extract_date_httpFormat(each_date['to'])
		elif(ppt_date['d_id'] == 'interview_date'):
			interview_date_from = extract_date_httpFormat(each_date['from'])
			interview_date_to = extract_date_httpFormat(each_date['to'])

	class ScheduleForm(FlaskForm):
		ppt_date = DateField('PPT date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form', 'min':ppt_date_from, 'max':ppt_date_to})
		test_date = DateField('Test date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form', 'min':test_date_from, 'max':test_date_to})
		interview_date = DateField('Interview Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form', 'min':interview_date_from, 'max':interview_date_to})
		ppt_link = StringField('PPT Link', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
		test_link = StringField('Test Link', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
		interview_link = StringField('Interview Link', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
		submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
	form = ScheduleForm()
	if form.validate_on_submit():
		ppt_date = form.ppt_date.data
		test_date = form.test_date.data
		interview_date = form.interview_date.data
		ppt_link = form.ppt_link.data
		test_link = form.test_link.data
		interview_link = form.interview_link.data
		role_id = strToInt(role_id)
		sql1 = f"INSERT INTO schedule(ppt_date, test_date, interview_date, ppt_link, test_link, interview_link) VALUES('{ppt_date}', '{test_date}', '{interview_date}', '{ppt_link}', '{test_link}', '{interview_link}') RETURNING schedule_id"
		schedule_id=db.engine.execute(sql1).first()['schedule_id']
		db.session.commit()
		sql2 = f"UPDATE role SET schedule_id = {schedule_id} WHERE role_id={role_id}"
		db.engine.execute(sql2)
		db.session.commit()
		return redirect(url_for('role.roles_eligibilty',role_id=role_id))
		#return redirect(url_for('main.home'))
	return render_template('schedule_create.html', form = form)

@role.route('/roles/<string:role_id>', methods = ['GET', 'POST'])
@login_required
def roles_eligibilty(role_id):
	form = RolesEligibilityForm()
	role_id = strToInt(role_id)
	sql = f"SELECT branch,cgpa FROM roles_eligibility WHERE role_id={role_id};"
	res = db.engine.execute(sql)
	if form.validate_on_submit():
		branch=form.branch.data
		cgpa=form.cgpa.data
		sql1 = f"INSERT INTO roles_eligibility(role_id,branch,cgpa) VALUES ('{role_id}','{branch}','{cgpa}')"
		db.engine.execute(sql1)
		db.session.commit()
		return redirect(url_for('role.roles_eligibilty',role_id=role_id))
	return render_template('roles_eligibility.html',form=form,res=res)
