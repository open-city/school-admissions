from flask import Blueprint, make_response, request, jsonify, \
    session as flask_session
import json
from sqlalchemy import Table
from api.database import session, engine, Base

endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/api/')
def source():
    start = request.args.get('start')
    end = request.args.get('end')
    resp = {
        'meta': {
            'status': 'ok',
            'message': ''
        }
    }
    if not start or end:
        resp['meta']['status'] = 'error'
        resp['meta']['message'] = 'start and end are required'
    else:
        
        zone_table = Table('zone09_cmap_2009', Base.metadata, 
            autoload=True, autoload_with=engine, keep_existing=True)
        
    resp =  make_response(json.dumps({}))
    resp.headers['Content-Type'] = 'application/json'
    return resp
