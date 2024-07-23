from project import db
from datetime import datetime
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column(db.LargeBinary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    email_confirmation_sent_on = db.Column(db.DateTime, nullable=True)
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmed_on = db.Column(db.DateTime, nullable=True)
    registered_on = db.Column(db.DateTime, nullable=True)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    current_logged_in = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String, default='user')
    items = db.relationship("Items", back_populates="user")

    def __init__(self, email, password, authenticated=False, email_confirmation_sent_on=None, email_confirmed=False, email_confirmed_on=None, registered_on=None, last_logged_in=None, current_logged_in=None, role='user'):
        self.email = email
        self.password = password
        self.authenticated = authenticated
        self.email_confirmation_sent_on = email_confirmation_sent_on
        self.email_confirmed = email_confirmed
        self.email_confirmed_on = email_confirmed_on
        self.registered_on = registered_on if registered_on else datetime.now()
        self.last_logged_in = last_logged_in
        self.current_logged_in = current_logged_in if current_logged_in else datetime.now()
        self.role = role

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Bcrypt().generate_password_hash(password)

    @hybrid_method
    def is_correct_password(self, password):
        return Bcrypt().check_password_hash(self._password, password)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_email_confirmed(self):
        return self.email_confirmed

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.email)

class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="items")
    
    def __init__(self, name, notes, user_id):
        self.name = name
        self.notes = notes
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)
