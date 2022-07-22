from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
# =============================================================================
# class BasicInvoiceForm(FlaskForm):
#     numer_faktury = StringField('numer_faktury')
#     data_wystawienia = DateField('data_wystawienia')
#     data_sprzedaży = DateField('data_sprzedaży')
#     
#     sprzedawca = StringField('sprzedawca')
#     nip_sprzedawcy = IntegerField('nip_sprzedawcy')
#     miejscowosc_sprzedawcy = StringField('miejscowosc_sprzedawcy')
#     ulica_sprzedawcy = StringField('ulica')
#     kod_pocztowy_sprzedawcy = StringField('kod pocztowy')
#     
#     nabywca = StringField('nabywca')
#     nip_nabywcy = IntegerField('nip_nabywcy')
#     miejscowosc_nabywcy = StringField('miejscowosc_nabywcy')
#     ulica_nabywcy = StringField('ulica')
#     kod_pocztowy_nabywcy = StringField('kod pocztowy')
#     
#     nazwa_usługi = StringField('nazwa_usługi')
#     jednostka = StringField('jednostka')
#     ilosc = IntegerField('ilosc')
#     cena = IntegerField('cena')
#     
#     submit = SubmitField('Generuj')
#     
# =============================================================================

# =============================================================================
# class BasicInvoiceForm(FlaskForm):
#     numer_faktury = StringField('numer_faktury')
#     
#     nip_sprzedawcy = IntegerField('nip_sprzedawcy')
#   
#     nip_nabywcy = IntegerField('nip_nabywcy')
#  
#     submit = SubmitField('Generuj')
# =============================================================================

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