import hashlib
from backend.models.person import *
from backend.database.database import db


class Admin(Person):

    __tablename__ = 'admin'
    __mapper_args__ = {'polymorphic_identity': 'admin'}

    def __init__(self, first_name, last_name, birthday, gender, phone, password):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.phone = phone
        self.password = hashlib.sha256(
            password.encode("utf-8")).hexdigest()
        self.role = 'admin'
