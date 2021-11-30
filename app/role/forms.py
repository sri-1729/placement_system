from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, DateField
from flask import render_template, redirect, session, url_for
from wtforms.validators import DataRequired
# from wtforms.fields.html5 import DateField

class RoleForm(FlaskForm):
	title = StringField('Title', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	jd_link = StringField('Job Description Link', validators = [DataRequired()], render_kw = {'class':'input-form'})
	ctc = StringField('ctc', validators = [DataRequired()], render_kw = {'class':'input-form'})
	last_date = DateField('Last date to apply', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})

class ScheduleForm(FlaskForm):
	ppt_date = DateField('PPT date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	test_date = DateField('Test date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	interview_date = DateField('Interview Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	ppt_link = StringField('PPT Link', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	test_link = StringField('Test Link', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	interview_link = StringField('Interview Link', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
	
class RolesEligibilityForm(FlaskForm):
	branch = StringField('Branch', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	cgpa = DecimalField('CGPA', validators = [DataRequired()],rounding=2, render_kw = {'class':'input-form'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
