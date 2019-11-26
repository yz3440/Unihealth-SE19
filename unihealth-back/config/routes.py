from flask_restful import Api
from resources.user_handlers import (Register, Login, Logout)


def init_routes(app):
    api = Api(app)

    api.add_resource(Register, "/auth/register")

    api.add_resource(Login, "/auth/login")

    api.add_resource(Logout, '/auth/logout')
