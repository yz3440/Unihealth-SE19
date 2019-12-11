import logging
from datetime import datetime

from flask import request, after_this_request
from flask_restful import Resource

import error.errors as error
from config.auth import auth, refresh_jwt
from database.database import db
from models.person import Person
from models.patient import Patient
from models.doctor import Doctor
from models.token_blacklist import TokenBlacklist

from models.health_log import HealthLog


class User(Resource):

    # Register user with POST request
    @staticmethod
    def post():
        try:
            first_name, last_name, gender, birthday, phone, password = \
                request.json.get('firstName').strip(), request.json.get('lastName').strip(), \
                request.json.get('gender').strip(), request.json.get('birthday').strip(), \
                request.json.get('phone').strip(
                ),  request.json.get('password').strip()
            birthday = datetime.strptime(birthday, '%Y/%m/%d')

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

        return {'status': 'registration completed.'}

    # Login user with GET request
    @staticmethod
    def get():
        @after_this_request
        def set_token_cookie(response):
            response.set_cookie('access_token', access_token,
                                max_age=64800, httponly=True, path="/auth")
            response.set_cookie('refresh_token', refresh_token,
                                max_age=64800, httponly=True, path="/auth")
            return response

        try:
            phone, password = request.json.get(
                'phone').strip(), request.json.get('password').strip()

        except Exception as why:
            logging.info("Email or password is wrong. " + str(why))
            return error.INVALID_INPUT

        if phone is None or password is None:
            return error.INVALID_INPUT

        person = Person.query.filter_by(
            phone=phone).first()

        if person is None:
            return error.DOES_NOT_EXIST
        elif not person.verify_password(password):
            return error.INVALID_PASSWORD

        # Generate access token & refresh token
        access_token = person.generate_access_token()
        refresh_token = person.generate_refresh_token()

        # Return access token & refresh token.
        return {"msg": "Login successful."}, 200

    # Logout user with DELETE request
    @staticmethod
    @auth.login_required
    def delete():

        # Get refresh token.
        refresh_token = request.json.get('refresh_token')

        # Get if the refresh token is in blacklist
        ref = TokenBlacklist.query.filter_by(
            refresh_token=refresh_token).first()

        # Check refresh token has existed.
        if ref is not None:
            return {'status': 'already invalidated', 'refresh_token': refresh_token}

        # Create a blacklist refresh token.
        blacklist_refresh_token = TokenBlacklist(refresh_token=refresh_token)

        # Add refresh token to session.
        db.session.add(blacklist_refresh_token)

        # Commit session.
        db.session.commit()

        # Return status of refresh token.
        return {'status': 'invalidated', 'refresh_token': refresh_token}
