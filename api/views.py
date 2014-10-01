from flask import Blueprint, make_response, request, jsonify, \
    session as flask_session, render_template
import json
from sqlalchemy import Table, func, or_
from api.database import session, engine, Base
from api.models import SourceDest

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')
