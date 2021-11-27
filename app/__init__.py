from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager 

login_manager = LoginManager()
db = SQLAlchemy()
def create_app(config_name):

	#introduces the app
	app = Flask(__name__)

	#specify the configuration of the app from the config module
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	#connect app to SQLDatabase interface
	db.init_app(app)
	login_manager.init_app(app)

	#registering a blueprint
	#blueprint for home page
	from .main import main as m_bp
	app.register_blueprint(m_bp)
	#blueprint for authorization
	from .login import login as l_bp 
	app.register_blueprint(l_bp, url_prefix = '/auth')
	from .profile import profile as p_bp
	app.register_blueprint(p_bp, url_prefix = '/profile')
	
	return app