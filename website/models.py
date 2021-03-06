from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    invoices = db.relationship('Invoice', backref='creator', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numer_faktury = db.Column(db.String)
    
    sprzedawca = db.Column(db.String(120), index=True)
    nip_sprzedawcy = db.Column(db.Integer)
    
    nabywca = db.Column(db.String(120), index=True)
    nip_nabywcy = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Invoice {}, Sprzedawca {}, id_tworcy: {}>'.format(
            self.numer_faktury, self.sprzedawca, self.user_id)