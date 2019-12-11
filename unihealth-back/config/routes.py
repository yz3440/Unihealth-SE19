from flask_restful import Api
# from resources.user_handlers import (Register, Login, Logout)
from resources.user import User

from resources.health_logs import HealthLogs


def init_routes(app):
    api = Api(app)

    # User Handlers
    api.add_resource(User, "/auth/user")

    # Health Logs
    api.add_resource(HealthLogs, '/resources/health_logs')
