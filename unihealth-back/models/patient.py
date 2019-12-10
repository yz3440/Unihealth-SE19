import hashlib
from models.person import *
from database.database import db


class Patient(Person):
    __tablename__ = 'patient'
    __mapper_args__ = {'polymorphic_identity': 'patient'}

    def __init__(self, first_name, last_name, birthday, gender, phone, password):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.phone = phone
        self.password = hashlib.sha256(
            password.encode("utf-8")).hexdigest()
        self.role = 'patient'

    def __repr__(self):
        return "<Patient(phone='%s', name='%s %s', password='%s', created='%s')>" % (
            self.phone, self.first_name, self.last_name, self.password, self.email, self.created)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
