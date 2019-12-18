from database.database import db, ma
from datetime import datetime


class HealthLogType(db.Model):
    __tablename__ = 'health_log_type'

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)

    log_type = db.Column("type", db.String, unique=True, nullable=False)


class HealthLogTypeSchema(ma.ModelSchema):
    class Meta:
        model = HealthLogType
