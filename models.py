from app import db
# from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    """Users base model."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), nullable=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)
