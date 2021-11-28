from flask import Blueprint

#creating blueprint for app routes and error handling pages
role = Blueprint('role', __name__)
from . import views