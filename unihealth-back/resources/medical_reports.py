import logging

from flask import request, g
from flask_restful import Resource

import error.errors as error
from config.auth import auth
from database.database import db
from models.patient import Patient
from models.doctor import Doctor

from models.medical_report import MedicalReport, MedicalReportSchema

medical_report_schema = MedicalReportSchema()
medical_reports_schema = MedicalReportSchema(many=True)


class MedicalReports(Resource):

    @staticmethod
    @auth.login_required
    def get():
        # User being a patient
        if g.admin == 0:
            owner_phone = g.user

        # User being a doctor or admin
        else:
            try:
                owner_phone = request.args.get('phone').strip()

            except Exception as why:
                logging.info("The user input is invalid. " + str(why))
                return error.INVALID_INPUT

        patient = Patient.query.filter_by(phone=owner_phone).first()

        medical_reports = MedicalReport.query.filter_by(
            owner_id=patient.id).all()

        # Serializing response
        response = medical_reports_schema.dump(medical_reports)

        return response

    @staticmethod
    @auth.login_required
    def post():
        # User has to be doctor to modify the health reports
        if g.admin == 0:
            return error.UNAUTHORIZED_ACCESS
        else:
            reporter_id = Doctor.query.filter_by(phone=g.user).first().id
        try:
            owner_phone, disease, note = request.json.get('phone').strip(),\
                request.json.get('disease').strip(), \
                request.json.get('note').strip()

        except Exception as why:
            logging.info("The user input is invalid. " + str(why))
            return error.INVALID_INPUT

        owner = Patient.query.filter_by(phone=owner_phone).first()
        if owner is None:
            return error.DOES_NOT_EXIST
        owner_id = Patient.query.filter_by(phone=owner_phone).first().id

        medical_report = MedicalReport(
            owner_id=owner_id, reporter_id=reporter_id, disease=disease, note=note)

        db.session.add(medical_report)
        db.session.commit()

        return {'msg': 'The medical report has been added.', 'reportId': medical_report.id}
