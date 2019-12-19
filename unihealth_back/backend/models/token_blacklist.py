from backend.database.database import db


class TokenBlacklist(db.Model):

    __tablename__ = 'token_blacklist'

    id = db.Column(db.Integer, primary_key=True)

    refresh_token = db.Column(db.String(length=255))

    def __repr__(self):
        # This is only for representation how you want to see refresh tokens after query.
        return "<Person(id='%s', refresh_token='%s', status='invalidated.')>" % (
            self.id, self.refresh_token)
