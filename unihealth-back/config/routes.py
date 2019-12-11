from flask_restful import Api
from resources.user import User
from resources.token import Token
from resources.health_logs import HealthLogs
from resources.health_log_types import HealthLogTypes


def init_routes(app):
    api = Api(app)

    # User data
    api.add_resource(User, "/resources/user")

    # Access Token Generation
    api.add_resource(Token, "/auth/token")

    # Health Logs
    api.add_resource(HealthLogs, '/resources/health_logs')
    api.add_resource(HealthLogTypes, '/resources/health_log_types')
