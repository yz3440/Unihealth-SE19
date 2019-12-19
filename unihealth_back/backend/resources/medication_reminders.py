import logging
from datetime import datetime, timedelta

from flask import request, g
from flask_restful import Resource

import backend.error.errors as error
from backend.config.auth import auth
from backend.database.database import db
from backend.models.patient import Patient
from backend.models.doctor import Doctor

from backend.models.medication_reminder import MedicationReminder, MedicationReminderSchema

medication_reminder_schema = MedicationReminderSchema()
medication_reminders_schema = MedicationReminderSchema(many=True)

# Generate detailed reminders from medication reminders within the timedelta from now


class MedicationReminders(Resource):
    @staticmethod
    @auth.login_required
    def post():
        # User has to be doctor to modify the health reports
        if g.admin == 0:
            return error.UNAUTHORIZED_ACCESS

        try:
            disease, start, end, medicine, amount, periodicity, owner_phone = request.json.get('disease').strip(), request.json.get('start').strip(),\
                request.json.get('end').strip(), request.json.get('medicine').strip(),\
                request.json.get('amount').strip(), request.json.get(
                    'periodicity').strip(), request.json.get(
                    'phone').strip()
            start = datetime.strptime(start, '%Y-%m-%d')
            end = datetime.strptime(end, '%Y-%m-%d')
            periodicity = int(periodicity)

        except Exception as why:
            logging.info("The user input is invalid. " + str(why))
            return error.INVALID_INPUT

        owner = Patient.query.filter_by(phone=owner_phone).first()
        if owner is None:
            return error.DOES_NOT_EXIST
        owner_id = Patient.query.filter_by(phone=owner_phone).first().id

        medication_reminder = MedicationReminder(
            disease=disease, start=start, end=end, medicine=medicine, amount=amount, periodicity=periodicity, owner_id=owner_id)

        db.session.add(medication_reminder)
        db.session.commit()

        return {'msg': 'The medication reminder has been added.'}

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

        medicaiton_reminders = MedicationReminder.query.filter_by(
            owner_id=patient.id).all()

        # Generate Detailed Reminders from Medication Reminders
        reminders = generate_detailed_reminders(
            medicaiton_reminders, timedelta(weeks=1))

        return reminders


def generate_detailed_reminders(medicaiton_reminders, within_timedelta):
    today = datetime.utcnow()
    reminders = []
    for medication in medicaiton_reminders:
        periodicity = timedelta(hours=medication.periodicity)
        in_take_time = medication.start
        while in_take_time < (today+within_timedelta):
            in_take_time += periodicity
            if in_take_time > today:
                reminders.append({"medicine": medication.medicine, "disease": medication.disease,
                                  "amount": medication.amount, "created": in_take_time.isoformat(), "periodicity": medication.periodicity})
    reminders.sort(reverse=True, key=lambda reminder: reminder['created'])
    return reminders
