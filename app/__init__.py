from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()
def create_app(config_name):

	#introduces the app
	app = Flask(__name__)

	#specify the configuration of the app from the config module
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	#connect app to SQLDatabase interface
	#db.init_app(app)

	#registering a blueprint
	from .main import main as m_bp
	app.register_blueprint(m_bp)

	return app