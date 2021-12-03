from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField
from flask import render_template, redirect, session, url_for
from wtforms.validators import DataRequired
from .. import db

#ProfileForm used for Edit Profile and View Profile Page
class ProfileFormI(FlaskForm):
	fname = StringField('First Name', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	lname = StringField('Last Name', validators = [DataRequired()], render_kw = {'class':'input-form'})
	cgpa = DecimalField('CGPA', validators = [DataRequired()],rounding=2, render_kw = {'class':'input-form'})
	branch = StringField('Branch', validators = [DataRequired()], render_kw = {'class':'input-form'})
	resume_link = StringField('Resume Link', validators = [DataRequired()], render_kw = {'class':'input-form'})
	contact_no = StringField('Contact Number', validators = [DataRequired()], render_kw = {'class':'input-form'})
	email = StringField('Email', validators = [DataRequired()], render_kw = {'class':'input-form'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
	
#CompanyForm used for Company Page
class CompanyFormI(FlaskForm):
	company_name=StringField('Company Name', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	company_link=StringField('Company Description Link', validators = [DataRequired()], render_kw = {'class':'input-form'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})



# class ProfileFormE(FlaskForm):
# 	fname = StringField('First Name', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form', 'value':prof['fname']})
# 	lname = StringField('Last Name', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['lname']})
# 	cgpa = DecimalField('CGPA', validators = [DataRequired()],rounding=2, render_kw = {'autocomplete':'off','class':'input-form', 'value':str(prof['cgpa'])})
# 	branch = StringField('Branch', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['branch']})
# 	resume_link = StringField('Resume Link', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['resume_link']})
# 	contact_no = StringField('Contact Number', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['contact_no']})
# 	email = StringField('Email', validators = [DataRequired()], render_kw = {'autocomplete':'off','class':'input-form', 'value':prof['email_id']})
# 	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
