import enum

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Event_Type(enum.Enum):
    Create = 1
    Update = 2
    Delete = 3


class EventStore(db.Model):
    __tablename__ = "event_store"
    __bind_key__ = 'event_store'
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.Enum(Event_Type))
    prescription_doctor_id = db.Column(db.String(50), nullable=False)
    prescription_patient_id = db.Column(db.String(20), nullable=False)
    prescription_drug = db.Column(db.String(50))
    prescription_comment = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        vals = vars(self)
        dic = {attr: vals[attr] for attr in vals if 'instance_state' not in attr}
        dic['event_type'] = str(dic['event_type'])
        return dic


class Prescription(db.Model):
    __tablename__ = "prescription"
    __bind_key__ = 'prescriptions'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.String(50), nullable=False)
    patient_id = db.Column(db.String(20), nullable=False)
    drug = db.Column(db.String(50))
    comment = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        vals = vars(self)
        return {attr: vals[attr] for attr in vals if 'instance_state' not in attr}
