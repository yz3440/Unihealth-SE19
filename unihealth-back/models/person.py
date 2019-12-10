import hashlib
from datetime import datetime

from flask import g

from config.authentication import auth, jwt, refresh_jwt
from database.database import db


class Person(db.Model):

    __tablename__ = 'person'

    # User phone number as primary key.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column('first_name', db.String, nullable=False)
    last_name = db.Column('last_name', db.String, nullable=False)
    gender = db.Column("gender", db.String, nullable=False)
    birthday = db.Column("birthday", db.Date, nullable=False)
    phone = db.Column('phone', db.String, unique=True, nullable=False)
    password = db.Column('password', db.String, nullable=False)

    created = db.Column(db.DateTime, default=datetime.utcnow)

    # Unless otherwise stated default role is patient.
    role = db.Column('role', db.String, nullable=False, default='patient')
    __mapper_args__ = {'polymorphic_on': role}

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

    def __repr__(self):
        return "<Person(phone='%s', fullname='%s', password='%s', created='%s', role='%s')>" % (
            self.phone, self.fullname, self.password, self.email, self.created, self.role)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
