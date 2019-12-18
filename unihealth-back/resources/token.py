import logging
from datetime import datetime

from flask import request
from flask_restful import Resource

import error.errors as error
from config.auth import auth, refresh_jwt
from database.database import db
from models.person import Person
from models.token_blacklist import TokenBlacklist


class Token(Resource):

    # Login user and get the jwt with POST request
    @staticmethod
    def post():
        try:
            phone, password = request.json.get(
                'phone').strip(), request.json.get('password').strip()

        except Exception as why:
            logging.info("Phone or password is wrong. " + str(why))
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
        return {"msg": "Login successful.", "access_token": access_token.decode('utf-8'), "refresh_token": refresh_token.decode('utf-8')}, 200

    # Refresh user and get the jwt with PUT request
    @staticmethod
    def put():
        try:
            # Get refresh token.
            refresh_token = request.json.get('refresh_token').encode('utf-8')
            print(refresh_token)
        except Exception:
            return error.INVALID_INPUT

        data = refresh_jwt.loads(refresh_token)

        # Check if phone variables is in refresh token.
        if 'phone' not in data:
            return error.INVALID_INPUT

        person = Person.query.filter_by(phone=data['phone']).first()

        if person is None:
            return error.DOES_NOT_EXIST

        # Generate access token & refresh token
        access_token = person.generate_access_token()
        refresh_token = person.generate_refresh_token()

        # Return access token & refresh token.
        return {"msg": "Refresh successful.", "access_token": access_token.decode('utf-8'), "refresh_token": refresh_token.decode('utf-8')}, 200

    # Logout user and delete the jwt with DELETE request
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
        return {'msg': 'Refresh token invalidated.', 'refresh_token': refresh_token}
