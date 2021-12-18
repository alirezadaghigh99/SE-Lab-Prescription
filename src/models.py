import enum

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event_Type(enum.Enum):
    Create = 1
    Update = 2
    Delete = 3


class EventStore(db.Model):
    __tablename__ = "event_store"
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Colunmn(db.Enum(Event_Type))
    prescription_doctor_id = db.Column(db.String(50), nullable=False)
    prescription_patient_id = db.Column(db.String(20), nullable=False)
    prescription_drug = db.Column(db.String(50))
    prescription_comment = db.Column(db.String(100))
    prescription_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        vals = vars(self)
        dic = {attr: vals[attr] for attr in vals if 'instance_state' not in attr}
        dic['event_type'] = str(dic['event_type'])
        return dic


class Prescription(db.Model):
    __tablename__ = "prescription"
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.String(50), nullable=False)
    patient_id = db.Column(db.String(20), nullable=False)
    drug = db.Column(db.String(50))
    comment = db.Column(db.String(100))

    def to_dict(self):
        vals = vars(self)
        return {attr: vals[attr] for attr in vals if 'instance_state' not in attr}
