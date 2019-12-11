import logging
from datetime import datetime

from flask import request, g
from flask_restful import Resource

import error.errors as error
from config.auth import auth, refresh_jwt
from database.database import db
from models.person import Person, PersonSchema
from models.patient import Patient
from models.doctor import Doctor

person_schema = PersonSchema()


class User(Resource):

    # Register user with POST request
    @staticmethod
    def post():
        print(request.json)

        try:
            first_name, last_name, gender, birthday, phone, password = \
                request.json.get('firstName').strip(), request.json.get('lastName').strip(), \
                request.json.get('gender').strip(), request.json.get('birthday').strip(), \
                request.json.get('phone').strip(
                ),  request.json.get('password').strip()
            birthday = datetime.strptime(birthday, '%Y-%m-%d')

        except Exception as why:
            logging.info("The user input is invalid. " + str(why))
            return error.INVALID_INPUT

        if not first_name or not last_name or not gender or not birthday or not phone or not password:
            return error.INVALID_INPUT

        person = Person.query.filter_by(phone=phone).first()

        if person is not None:
            return error.ALREADY_EXIST

        person = Patient(first_name=first_name, last_name=last_name, gender=gender,
                         birthday=birthday, phone=phone, password=password)

        db.session.add(person)
        db.session.commit()

        return {'msg': 'Registration Completed.'}, 200

    # Get user info with GET request
    @staticmethod
    @auth.login_required
    def get():

        person = Person.query.filter_by(phone=g.user).first()

        # Serializing person's data
        response = person_schema.dump(person)

        return response
