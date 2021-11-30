from flask import Blueprint

#creating blueprint for app routes and error handling pages
admin = Blueprint('admin', __name__)
from . import views
