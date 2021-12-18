from flask import Blueprint, request
from flask.json import jsonify
from models import Prescription

query_handler = Blueprint('Query Handler', __name__)


@query_handler.route('/prescription/query', methods=['GET'])
def read_prescriptions():
    query = Prescription.query
    if 'doctor_id' in request.args:
        query = query.filter_by(doctor_id=request.args['doctor_id'])
    if 'patient_id' in request.args:
        query = query.filter_by(patient_id=request.args['patient_id'])
    if 'admin_username' in request.args:
        query = query.all()

    return jsonify([prescription.to_dict() for prescription in query.all()])
