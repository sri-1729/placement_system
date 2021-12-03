from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, SelectField
from flask import render_template, redirect, session, url_for
from wtforms.validators import DataRequired

#RegisterForm used for Register Page
class RegisterForm(FlaskForm):
	userId = StringField('userid', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	password = PasswordField('password', validators = [DataRequired()], render_kw = {'class':'input-form'})
	cpassword = PasswordField('confirm password', validators = [DataRequired()], render_kw = {'class':'input-form'})
	type_ = SelectField('type', choices=[('student', 'student'),('company','company')], validators = [DataRequired()], render_kw = {'class':'custom-select'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
