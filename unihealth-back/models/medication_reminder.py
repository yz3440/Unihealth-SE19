from database.database import db, ma
from datetime import datetime


class MedicationReminder(db.Model):
    __tablename__ = 'medication_reminder'

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column("owner_id", db.Integer,
                         db.ForeignKey('person.id'), nullable=False)

    disease = db.Column("disease", db.String, nullable=False)
    medicine = db.Column("medicine", db.String, nullable=False)

    start = db.Column("start", db.DateTime,
                      default=datetime.utcnow, nullable=False)

    end = db.Column("end", db.DateTime, nullable=True)

    amount = db.Column("amount", db.String, nullable=False)

    # The medicine should be taken every k hours
    periodicity = db.Column("periodicity", db.Integer, nullable=False)

    is_canceled = db.Column("is_canceled", db.Boolean,
                            default=False, nullable=False)
    created = db.Column("created", db.DateTime, default=datetime.utcnow)


class MedicationReminderSchema(ma.ModelSchema):
    class Meta:
        model = MedicationReminder
