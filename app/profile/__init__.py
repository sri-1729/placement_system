from flask import Blueprint

#creating blueprint for app routes and error handling pages
profile = Blueprint('profile', __name__)
from . import views