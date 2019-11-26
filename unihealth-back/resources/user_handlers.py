import logging
import hashlib
from datetime import datetime

from flask import request
from flask_restful import Resource

import error.errors as error
from config.authentication import auth, refresh_jwt
from database.database import db
from models.person import Person
from models.patient import Patient
from models.doctor import Doctor
from models.token_blacklist import TokenBlacklist


class Register(Resource):
    @staticmethod
    def post():
        try:
            phone, fullname, password = request.json.get('phone').strip(), request.json.get('fullname').strip(), \
                request.json.get('password').strip()

        except Exception as why:
            logging.info("Phone, fullname or password is wrong. " + str(why))
            return error.INVALID_INPUT

        if phone is None or fullname is None or password is None:
            return error.INVALID_INPUT

        person = Person.query.filter_by(phone=phone).first()

        if person is not None:
            return error.ALREADY_EXIST

        # Encrypts password
        hashedPassword = hashlib.sha256(
            password.encode("utf-8")).hexdigest()

        person = Patient(phone=phone, fullname=fullname,
                         password=hashedPassword)

        db.session.add(person)
        db.session.commit()

        return {'status': 'registration completed.'}


class Login(Resource):
    @staticmethod
    def post():

        try:
            phone, password = request.json.get(
                'phone').strip(), request.json.get('password').strip()

        except Exception as why:
            logging.info("Email or password is wrong. " + str(why))
            return error.INVALID_INPUT

        if phone is None or password is None:
            return error.INVALID_INPUT

        # Encrypts password
        hashedPassword = hashlib.sha256(
            password.encode("utf-8")).hexdigest()
        person = Person.query.filter_by(
            phone=phone, password=hashedPassword).first()

        if person is None:
            return error.DOES_NOT_EXIST

        access_token = person.generate_auth_token()

        # Generate refresh token.
        refresh_token = refresh_jwt.dumps({'phone': phone})

        # Return access token and refresh token.
        return {'access_token': str(access_token), 'refresh_token': str(refresh_token)}


class Logout(Resource):
    @staticmethod
    @auth.login_required
    def post():

        # Get refresh token.
        refresh_token = request.json.get('refresh_token')

        # Get if the refresh token is in blacklist
        ref = TokenBlacklist.query.filter_by(
            refresh_token=refresh_token).first()

        # Check refresh token is existed.
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
