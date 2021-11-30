from flask import Blueprint

#creating blueprint for app routes and error handling pages
jobs = Blueprint('jobs', __name__)
from . import views