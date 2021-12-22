from flask import Blueprint, request
from flask.json import jsonify
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from models import *
from event_handler import bus

command_handler = Blueprint('Command Handler', __name__)


def pres_exists_checker(id):
    event = EventStore.filter_by(prescription_id=id).all()
    return len(event) != 0


@command_handler.route("/prescription", methods=["POST"])
def create_prescription():
    data = request.json
    if pres_exists_checker(data["prescription_id"]):
        return {'message': 'Error: prescription_id is already exists!'}, HTTPStatus.CONFLICT

    event = EventStore(
        prescription_doctor_id=data["doctor_id"],
        prescription_id=data["id"],
        prescription_patient_id=data["patient_id"],
        prescription_drug=data["drug"],
        prescription_comment=data["comment"],
        event_type=Event_Type["Create"]

    )
    try:
        db.session.add(event)
        db.session.commit()
        bus.emit("create:prescription", event)
        return jsonify({"message": "success"}), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.BAD_REQUEST
