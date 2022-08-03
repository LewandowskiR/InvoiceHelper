from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Nazwa Użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Zaloguj')
    

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
    
    platnosc = StringField('sposob platnosci')
    nr_konta = IntegerField('nr konta')
    
    file = FileField('file', validators=[Optional()])
    
    submit = SubmitField('Generuj')
    
class RegistrationForm(FlaskForm):
    username = StringField('Nazwa Użytkownika', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    password2 = PasswordField(
        'Powtórz Hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Nazwa uzytkownika zajęta.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Adres e-mail jest już wykorzystany.')