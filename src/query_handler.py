from flask import Blueprint, request
from flask.json import jsonify
from models import Prescription

query_handler = Blueprint('Query Handler', __name__)


@query_handler.route('/prescription/query', methods=['GET'])
def read_prescriptions():
    query = Prescription.query
    if request.args["role"] == "doctor":
        query = query.filter_by(doctor_id=request.args['national_id'])
    if request.args["role"] == "patient":
        query = query.filter_by(patient_id=request.args['national_id'])
    if request.args["role"] == "admin":
        pass
    return jsonify([prescription.to_dict() for prescription in query.all()])
