from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

#LoginForm used in Login Page
class LoginForm(FlaskForm):
	userId = StringField('userid', validators = [DataRequired()], render_kw = {'autocomplete':'off', 'class':'input-form'})
	password = PasswordField('password', validators = [DataRequired()], render_kw = {'class':'input-form'})
	submit = SubmitField('Submit', render_kw = {'class':'submit-button'})
