import hashlib
from datetime import datetime

from flask import g

from config.auth import auth, jwt, refresh_jwt
from database.database import db, ma


class Person(db.Model):

    __tablename__ = 'person'

    # User phone number as primary key.
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column('first_name', db.String, nullable=False)
    last_name = db.Column('last_name', db.String, nullable=False)
    gender = db.Column("gender", db.String, nullable=False)
    birthday = db.Column("birthday", db.Date, nullable=False)
    phone = db.Column('phone', db.String, unique=True, nullable=False)
    password = db.Column('password', db.String, nullable=False)

    created = db.Column("created", db.DateTime, default=datetime.utcnow)

    # Unless otherwise stated default role is patient.
    role = db.Column('role', db.String, nullable=False, default='patient')
    __mapper_args__ = {'polymorphic_on': role}

    # Other tables
    owned_health_logs = db.relationship(
        'HealthLog', backref='owner', lazy='dynamic', foreign_keys='HealthLog.owner_id')
    reported_health_logs = db.relationship(
        'HealthLog', backref='reporter', lazy='dynamic', foreign_keys='HealthLog.reporter_id')
    # owned_medical_reports = db.relationship(
    #     'MedicalReport', backref='owner', lazy='dynamic', foreign_keys='MedicalReport.owner_id')
    # reported_medical_reports = db.relationship(
    #     'MedicalReport', backref='reporter', lazy='dynamic', foreign_keys='MedicalReport.reporter_id')

    def verify_password(self, password):
        hashedPassword = hashlib.sha256(
            password.encode("utf-8")).hexdigest()
        return hashedPassword == self.password

    # Generates access token.
    def generate_access_token(self):

        if self.role == 'doctor':
            # Generate doctor token with flag 1.
            token = jwt.dumps({'phone': self.phone, 'admin': 1})
            return token

        elif self.role == 'admin':
            # Generate admin token with flag 2.
            token = jwt.dumps({'phone': self.phone, 'admin': 2})
            return token

        # Return normal patient flag.
        return jwt.dumps({'phone': self.phone, 'admin': 0})

    # Generates refresh token.
    def generate_refresh_token(self):
        return refresh_jwt.dumps({'phone': self.phone})

    # Generates a new access token from refresh token.
    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):

        # Create a global none user.
        g.user = None

        try:
            # Load token.
            data = jwt.loads(token)

        except:
            # If any error return false.
            return False

        # Check if phone and admin permission variables are in jwt.
        if 'phone' and 'admin' in data:

            # Set phone from jwt.
            g.user = data['phone']

            # Set admin permission from jwt.
            g.admin = data['admin']

            # Return true.
            return True

        # If does not verified, return false.
        return False


class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id', "first_name", "last_name",
                  "birthday", "gender", "phone", "role")
