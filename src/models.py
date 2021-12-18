import enum

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event_Type(enum.Enum):
    Create = 1
    Update = 2
    Delete = 3

class EventStore(db.Model):
    __tablename__ = "event_store"
    event_type = db.Colunmn(db.Enum(Event_Type))

