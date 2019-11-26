from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JWT

# JWT creation.
jwt = JWT('jwt_top_secret', expires_in=3600)

# Refresh token creation.
refresh_jwt = JWT('refresh_jwt_top_secret', expires_in=7200)

# Auth object creation.
auth = HTTPTokenAuth('Bearer')
