from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    

class BasicInvoiceForm(FlaskForm):
    data_wystawienia = StringField('data_wystawienia')
    data_sprzedazy = StringField('data_sprzedazy')
    numer_faktury = StringField('numer_faktury')
    
    sprzedawca = StringField('sprzedawca')
    nip_sprzedawcy = IntegerField('nip_sprzedawcy')
    miejscowosc_sprzedawcy = StringField('miejscowosc_sprzedawcy')
    ulica_sprzedawcy = StringField('ulica')
    kod_pocztowy_sprzedawcy = StringField('kod pocztowy')
    
    nabywca = StringField('nabywca')
    nip_nabywcy = IntegerField('nip_nabywcy')
    miejscowosc_nabywcy = StringField('miejscowosc_nabywcy')
    ulica_nabywcy = StringField('ulica')
    kod_pocztowy_nabywcy = StringField('kod pocztowy')
    
    nazwa_usługi = StringField('nazwa_usługi')
    jednostka = StringField('jednostka')
    ilosc = IntegerField('ilosc')
    cena = IntegerField('cena')
    
    submit = SubmitField('Generuj')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')