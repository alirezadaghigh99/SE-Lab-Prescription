from flask import Blueprint, request
from flask.json import jsonify
from models import Prescription
from datetime import date
from sqlalchemy import func
from http import HTTPStatus

query_handler = Blueprint('Query Handler', __name__)


@query_handler.route("/")
def init():
    return "hello"


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


@query_handler.route('/prescription/stats', methods=['GET'])
def prescriptions_stats():
    query = Prescription.query
    try:
        day = int(request.args["day"])
        month = int(request.args["month"])
        year = int(request.args["year"])
        date_obj = date(year, month, day)
    except:
        return jsonify({"message": "Bad request"}), HTTPStatus.BAD_REQUEST
    query = query.filter(func.DATE(Prescription.timestamp) == date_obj)
    return jsonify([prescription.to_dict() for prescription in query.all()])
