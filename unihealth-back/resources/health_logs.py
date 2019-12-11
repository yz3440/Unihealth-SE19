import logging
from datetime import datetime

from flask import request
from flask_restful import Resource
from flask import g


import error.errors as error
from config.auth import auth, refresh_jwt
from database.database import db
from models.person import Person
from models.patient import Patient
from models.health_log import HealthLog, HealthLogSchema

health_log_schema = HealthLogSchema()
health_logs_schema = HealthLogSchema(many=True)


class HealthLogs(Resource):

    @staticmethod
    @auth.login_required
    def get():
        # User being a patient
        if g.admin == 0:
            owner_phone = g.user

        # User being a doctor or admin
        else:
            try:
                owner_phone = request.json.get('phone').strip()

            except Exception as why:
                logging.info("The user input is invalid. " + str(why))
                return error.INVALID_INPUT

        patient = Patient.query.filter_by(phone=owner_phone).first()

        health_logs = patient.owned_health_logs.all()

        # Serializing response
        response = health_logs_schema.dump(health_logs)

        return response

    @staticmethod
    @auth.login_required
    def post():
        # Check if user being a patient and self-reporting.
        if g.admin == 0:
            owner_id = Person.query.filter_by(phone=g.user).first().id
            reporter_id = owner_id

        # Check if user being a doctor or admin reporting for a patient.
        else:
            reporter_id = Person.query.filter_by(
                phone=g.user).first().id
            try:
                owner_phone = request.json.get('phone').strip(),
            except Exception as why:
                logging.info("The user input is invalid. " + str(why))
                return error.INVALID_INPUT

            owner = Person.query.filter_by(phone=owner_phone).first()
            # Check the patient being reported exists.
            if owner is None:
                return error.DOES_NOT_EXIST

        try:
            log_type, log_value = request.json.get(
                'type').strip(), request.json.get('value').strip()

        except Exception as why:
            logging.info("The user input is invalid. " + str(why))
            return error.INVALID_INPUT

        if not log_value.isnumeric():
            return error.INVALID_INPUT

        health_log = HealthLog(
            owner_id=owner_id, reporter_id=reporter_id, log_type=log_type, log_value=log_value)

        db.session.add(health_log)
        db.session.commit()

        return {'msg': 'The health log has been added.'}
