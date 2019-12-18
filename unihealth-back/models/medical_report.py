from database.database import db, ma
from datetime import datetime


class MedicalReport(db.Model):
    __tablename__ = 'medical_report'

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)

    owner_id = db.Column("owner_id", db.Integer,
                         db.ForeignKey('person.id'), nullable=False)

    reporter_id = db.Column("reporter_id", db.Integer,
                            db.ForeignKey('person.id'), nullable=True)

    disease = db.Column("disease", db.String, nullable=False)

    note = db.Column("note", db.String, nullable=False)

    created = db.Column("created", db.DateTime, default=datetime.utcnow)

    # suggested_medications = db.relationship(
    #     'MedicationReminder', backref='report', lazy='dynamic', foreign_keys='MedicationReminder.report_id')


class MedicalReportSchema(ma.ModelSchema):
    class Meta:
        model = MedicalReport
