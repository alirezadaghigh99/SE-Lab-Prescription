from flask import Blueprint, request, jsonify
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from models import *
from event_handler import bus

command_handler = Blueprint('Command Handler', __name__)


@command_handler.route("/prescription", methods=["POST"])
def create_prescription():
    data = request.json

    event = EventStore(
        prescription_doctor_id=data["doctor_id"],
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
