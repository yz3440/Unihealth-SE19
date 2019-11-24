#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Api

from api.handlers.UserHandlers import (AddUser, DataAdminRequired,
                                       DataUserRequired, Login, Logout,
                                       RefreshToken, Register, ResetPassword,
                                       UsersData)


def generate_routes(app):

    # Create api.
    api = Api(app)

    # Add all routes resources.
    # Register page.
    api.add_resource(Register, '/auth/register')

    # Login page.
    api.add_resource(Login, '/auth/login')

    # Logout page.
    api.add_resource(Logout, '/auth/logout')

    # Refresh page.
    api.add_resource(RefreshToken, '/auth/refresh')

    # Password reset page. Not forgot.
    api.add_resource(ResetPassword, '/auth/password_reset')

    # Get users page with admin permissions.
    api.add_resource(UsersData, '/users')

    # Example admin handler for admin permission.
    api.add_resource(DataAdminRequired, '/data_admin')

    # Example user handler for user permission.
    api.add_resource(DataUserRequired, '/data_user')

    # Example user handler for user permission.
    api.add_resource(AddUser, '/user_add')
