from flask import Blueprint

#creating blueprint for app routes and error handling pages
about = Blueprint('about', __name__)
from . import views

