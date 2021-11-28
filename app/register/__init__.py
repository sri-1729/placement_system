from flask import Blueprint

#creating blueprint for app routes and error handling pages
register = Blueprint('register', __name__)
from . import views