from . import profile
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from .forms import ProfileFormI,CompanyFormI
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField
from flask import render_template, redirect, session, url_for
from wtforms.validators import DataRequired

@profile.route('/edit/', methods = ['GET', 'POST'])
@login_required
def edit_profile():
	sql1 = f"SELECT stu_uid from profile where stu_uid = '{session['user']['userid']}'"
	profile = db.engine.execute(sql1).first()
	sql4 = f"SELECT * FROM profile where stu_uid = '{session['user']['userid']}'"
	prof = db.engine.execute(sql4).first()
	form = ProfileFormI()
	if form.validate_on_submit():
		fname = form.fname.data
		lname = form.lname.data
		cgpa = form.cgpa.data
		branch = form.branch.data
		contact = form.contact_no.data
		email = form.email.data
		resume_link = form.resume_link.data
		#to check the profile is already created
		
		#if exists just update the table
		if profile:
			sql2 = f"UPDATE profile SET fname='{fname}', lname='{lname}', cgpa={cgpa}, branch='{branch}', contact_no='{contact}', email_id='{email}', resume_link='{resume_link}' WHERE stu_uid = '{profile['stu_uid']}'"
			db.engine.execute(sql2)
			db.session.commit()
		#if not exists insert to profile
		else:
			sql3 = f"INSERT INTO profile(stu_uid,fname,lname,cgpa,branch,contact_no,email_id,resume_link,placement_status) VALUES('{session['user']['userid']}', '{fname}', '{lname}', {cgpa}, '{branch}', '{contact}', '{email}', '{resume_link}', 'Not Placed')"
			db.engine.execute(sql3)
			db.session.commit()
		return redirect(url_for('main.home'))
	
	if not profile:
		form = ProfileFormI()
		return render_template('edit_profile.html',form=form)
	else:
		class ProfileFormE(FlaskForm):
			fname = StringField('First Name', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form', 'value':prof['fname']})
			lname = StringField('Last Name', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['lname']})
			cgpa = DecimalField('CGPA', validators = [DataRequired()],rounding=2, render_kw = {'autocomplete':'off','class':'input-form', 'value':str(prof['cgpa'])})
			branch = StringField('Branch', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['branch']})
			resume_link = StringField('Resume Link', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['resume_link']})
			contact_no = StringField('Contact Number', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['contact_no']})
			email = StringField('Email', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['email_id']})
			submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
		form = ProfileFormE()
		return render_template('edit_profile.html', form=form)

@profile.route('/view/', methods = ['GET', 'POST'])
@login_required
def view_profile():
	sql1 = f"SELECT * from profile where stu_uid = '{session['user']['userid']}'"
	profile = db.engine.execute(sql1).first()
	print(profile)
	
@profile.route('/com_profile/', methods = ['GET', 'POST'])
@login_required
def com_profile():
	sql1 = f"SELECT com_uid from company where com_uid = '{session['user']['userid']}'"
	profile = db.engine.execute(sql1).first()
	sql4 = f"SELECT * FROM company where com_uid = '{session['user']['userid']}'"
	prof = db.engine.execute(sql4).first()
	form = CompanyFormI()
	if form.validate_on_submit():
		company_name = form.company_name.data
		company_link = form.company_link.data
		
		if profile:
			sql2 = f"UPDATE company SET company_name='{company_name}', company_link='{company_link}' WHERE com_uid = '{profile['com_uid']}'"
			db.engine.execute(sql2)
			db.session.commit()
		#if not exists insert to profile
		else:
			sql3 = f"INSERT INTO company(com_uid,company_name,company_link) VALUES('{session['user']['userid']}', '{company_name}', '{company_link}')"
			db.engine.execute(sql3)
			db.session.commit()
		return redirect(url_for('main.home'))
	
	if not profile:
		form = CompanyFormI()
		return render_template('company.html',form=form)
	else:
		class CompanyFormE(FlaskForm):
			company_name = StringField('Company Name', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form', 'value':prof['company_name']})
			company_link = StringField('Company Link', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['company_link']})
			submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
		form = CompanyFormE()
		return render_template('company.html', form=form)

