import logging

from flask import request
from flask_restful import Resource
from flask import g

import error.errors as error
from config.auth import auth, refresh_jwt
from database.database import db

from models.health_log_type import HealthLogType, HealthLogTypeSchema

health_log_type_schema = HealthLogTypeSchema()
health_log_types_schema = HealthLogTypeSchema(many=True)


class HealthLogTypes(Resource):

    @staticmethod
    @auth.login_required
    def get():

        health_log_types = HealthLogType.query.all()

        # Serializing health log types
        response = health_log_types_schema.dump(health_log_types)

        return response

    @staticmethod
    @auth.login_required
    def post():
        # User has to be admin to modify the total types of health log
        if g.admin < 2:
            return error.UNAUTHORIZED_ACCESS

        try:
            log_type = request.json.get('type').strip()

        except Exception as why:
            logging.info("The user input is invalid. " + str(why))
            return error.INVALID_INPUT

        health_log_type = HealthLogType(log_type=log_type)

        db.session.add(health_log_type)
        db.session.commit()

        return {'msg': 'The health log type has been added.'}