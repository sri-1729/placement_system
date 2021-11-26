from flask import Blueprint

#creating blueprint for app routes and error handling pages
login = Blueprint('login', __name__)
from . import views