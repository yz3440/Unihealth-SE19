from models.person import *
from database.database import db


class Patient(Person):
    __tablename__ = 'patient'
    __mapper_args__ = {'polymorphic_identity': 'patient'}

    def __init__(self, fullname, phone, password):
        self.phone = phone
        self.fullname = fullname
        self.password = password
        self.role = 'patient'

    def __repr__(self):
        return "<Patient(phone='%s', fullname='%s', password='%s', created='%s')>" % (
            self.phone, self.fullname, self.password, self.email, self.created)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
