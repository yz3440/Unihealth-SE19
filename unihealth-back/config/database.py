from models.admin import Admin
from datetime import datetime


def init_database(db):
    admin = Admin(first_name="Hospital", last_name="Admin",
                  birthday=datetime.today(), gender="male", phone="admin", password="admin")
    db.session.add(admin)
    db.session.commit()
