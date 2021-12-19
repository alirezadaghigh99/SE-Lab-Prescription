from event_bus import EventBus
from models import db, Prescription

bus = EventBus()


@bus.on('create:prescription')
def create_prescription_event_handler(event):
    prescription = Prescription(id=event.id,
                                doctor_id=event.prescription_doctor_id,
                                patient_id=event.prescription_patient_id,
                                drug=event.prescription_drug,
                                comment=event.prescription_comment,
                                )
    db.session.add(prescription)
    db.session.commit()
