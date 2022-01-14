from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    zipcode = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Users(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    zipcode = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "zipcode": self.zipcode
        }


class Pets(Base):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(120), unique=False, nullable=True)
    michrochip = db.Column(db.String(120), unique=True, nullable=True)
    found_date = db.Column(db.String(120), unique=False, nullable=True)
    injured = db.Column(db.String(120), unique=False, nullable=True)
    possible_name = db.Column(db.String(120), unique=False, nullable=True)
    color = db.Column(db.String(120), unique=False, nullable=False)
    size = db.Column(db.String(120), unique=False, nullable=True)
    weight = db.Column(db.String(120), unique=False, nullable=True)
    picture = db.Column(db.String(120), unique=False, nullable=True)
    zipcode = db.Column(db.String(120), unique=False, nullable=False)
    post_creator = db.Column(db.String(120), unique=True, nullable=False)