from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	userId = StringField('Enter userid', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	password = PasswordField('Enter password', validators = [DataRequired()])
	submit = SubmitField('Submit')