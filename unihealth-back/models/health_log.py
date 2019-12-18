from database.database import db, ma
from datetime import datetime


class HealthLog(db.Model):

    __tablename__ = 'health_log'

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)

    owner_id = db.Column("owner_id", db.Integer,
                         db.ForeignKey('person.id'), nullable=False)

    reporter_id = db.Column("reporter_id", db.Integer,
                            db.ForeignKey('person.id'), nullable=True)

    log_type = db.Column("type", db.String, db.ForeignKey(
        'health_log_type.type'), nullable=False)

    log_value = db.Column("value", db.String, nullable=False)

    created = db.Column("created", db.DateTime, default=datetime.utcnow)


class HealthLogSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = HealthLog
