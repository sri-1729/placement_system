from flask import Blueprint

#creating blueprint for app routes and error handling pages
main = Blueprint('main', __name__)
from . import views, error