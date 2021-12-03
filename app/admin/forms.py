from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, DateField
from flask import render_template, redirect, session, url_for
from wtforms.validators import DataRequired

#Slot Form used in Approve Companies Page 
class SlotForm(FlaskForm):
	i_fromdate = DateField('Interview From Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	i_todate = DateField('Interview To Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	p_fromdate = DateField('PPT From Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	p_todate = DateField('PPT To Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	t_fromdate = DateField('Test From Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	t_todate = DateField('Test To Date', format='%Y-%m-%d', validators = [DataRequired()], render_kw = {'class':'input-form'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})


