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
people_schema = PersonSchema(many=True)


class User(Resource):

    # Register user with POST request
    @staticmethod
    def post():
        try:
            first_name, last_name, gender, birthday, phone, password, role = \
                request.json.get('firstName').strip(), request.json.get('lastName').strip(), \
                request.json.get('gender').strip(), request.json.get('birthday').strip(), \
                request.json.get('phone').strip(),  request.json.get(
                    'password').strip(), request.json.get('role').strip()
            birthday = datetime.strptime(birthday, '%Y-%m-%d')

        except Exception as why:
            logging.info("The user input is invalid. " + str(why))
            return error.INVALID_INPUT

        if not first_name or not last_name or not gender or not birthday or not phone or not password:
            return error.INVALID_INPUT

        person = Person.query.filter_by(phone=phone).first()

        if person is not None:
            return error.ALREADY_EXIST

        if role == 'patient':
            person = Patient(first_name=first_name, last_name=last_name, gender=gender,
                             birthday=birthday, phone=phone, password=password)
        else:
            person = Doctor(first_name=first_name, last_name=last_name, gender=gender,
                            birthday=birthday, phone=phone, password=password)

        db.session.add(person)
        db.session.commit()

        return {'msg': 'Registration Completed.'}, 200

    # Get user info with GET request
    @staticmethod
    @auth.login_required
    def get():
        if request.args is not None:
            # Try fetch if there is a phone parameter when the user is doctor or admin
            phone = request.args.get('phone')
            if phone is not None and g.admin > 0:
                person = Person.query.filter_by(phone=phone).first()
                if person is None:
                    return error.DOES_NOT_EXIST
                response = person_schema.dump(person)
                return response

            # Try fetch if there is a all_user parameter when the user is admin
            all_user = request.args.get('allUser')
            if all_user and g.admin == 2:
                people = Person.query.all()
                response = people_schema.dump(people)
                return response

        # If no additional payload found, return the user's own profile
        person = Person.query.filter_by(phone=g.user).first()
        response = person_schema.dump(person)
        return response
