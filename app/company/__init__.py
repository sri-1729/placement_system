from flask import Blueprint

#creating blueprint for app routes and error handling pages
company = Blueprint('company', __name__)
from . import views