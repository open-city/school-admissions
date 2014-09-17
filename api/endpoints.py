from flask import Blueprint, make_response, request, jsonify, \
    session as flask_session
import json
from sqlalchemy import Table, func, or_
from api.database import session, engine, Base
from api.models import SourceDest

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
    if not start or not end:
        resp['meta']['status'] = 'error'
        resp['meta']['message'] = 'start and end are required'
    else:
        start = start.split(',')
        end = end.split(',')
        zone_table = Table('zone09_cmap_2009', Base.metadata, 
            autoload=True, autoload_with=engine, keep_existing=True)
        query = session.query(zone_table.c.zone09)\
            .filter(or_(
                func.st_contains(zone_table.c.geom, 
                    func.st_pointfromtext('POINT(' + str(start[1]) + ' ' + str(start[0]) + ')', 4326)),
                func.st_contains(zone_table.c.geom, 
                    func.st_pointfromtext('POINT(' + str(end[1]) + ' ' + str(end[0]) + ')', 4326))
            ))
        start_zone, end_zone = [i[0] for i in query.all()]
        travel_time = session.query(SourceDest)\
            .filter(SourceDest.source == start_zone)\
            .filter(SourceDest.dest == end_zone).first()
        resp['travel_time'] = travel_time.as_dict()
    resp =  make_response(json.dumps(resp))
    resp.headers['Content-Type'] = 'application/json'
    return resp
