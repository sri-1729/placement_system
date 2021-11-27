from . import db
from . import login_manager



#Login Table
class Login(db.Model):
	__tablename__ = 'login'
	userid = db.Column(db.String(50), unique=True, primary_key=True)
	password = db.Column(db.String(50))
	type_ = db.Column(db.String(10))
	auth = db.Column(db.Boolean, default=False)

	def __init__(self, userid, password, type_,  auth):
		self.userid = userid
		self.password = password
		self.type_ = type_
		self.auth = auth

	def is_active(self):
		"""True, as all users are active."""
		return True

	def get_id(self):
		"""Return the email address to satisfy Flask-Login's requirements."""
		return self.userid

	def is_authenticated(self):
		"""Return True if the user is authenticated."""
		return self.auth
	def is_anonymous(self):
		"""False, as anonymous users aren't supported."""
		return False

@login_manager.user_loader
def load_user(userid):
	return Login.query.get(userid)


#Profile Table
class Profile(db.Model):
	__tablename__ = 'profile'
	stu_uid = db.Column(db.String(50), db.ForeignKey('login.userid'), primary_key=True)
	fname = db.Column(db.String(50))
	lname = db.Column(db.String(50))
	cgpa = db.Column(db.Float(2))
	branch = db.Column(db.String(5))
	contact_no = db.Column(db.String(13))
	email_id = db.Column(db.String(70))
	resume_link = db.Column(db.String())
	placement_status = db.Column(db.String(1))
