# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, send_from_directory, request, url_for
from flask_login import current_user, login_user, logout_user
from .models import User
from .forms import LoginForm, BasicInvoiceForm, RegistrationForm
from .pdfgenerator import BasicInvoiceGenerate
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/create', methods=['GET', 'POST'])
def createInvoice():
    form = BasicInvoiceForm()
    if form.validate_on_submit():
        formdata = {
            "data_wystawienia": form.data_wystawienia.data,
            "data_sprzedazy": form.data_sprzedazy.data,
            "sprzedawca": form.sprzedawca.data,
            "nabywca": form.nabywca.data,
            "nip_sprzedawcy": form.nip_sprzedawcy.data,
            "nip_nabywcy": form.nip_nabywcy.data,
            "ulica_sprzedawcy": form.ulica_sprzedawcy.data,
            "ulica_nabywcy": form.ulica_nabywcy.data,
            "miejscowosc_sprzedawcy": form.miejscowosc_sprzedawcy.data,
            "miejscowosc_nabywcy": form.miejscowosc_nabywcy.data,
            "kod_sprzedawcy": form.kod_pocztowy_sprzedawcy.data,
            "kod_nabywcy": form.kod_pocztowy_nabywcy.data,
            "numer_faktury": form.numer_faktury.data,
            "nazwa_uslugi": form.nazwa_usługi.data,
            "jednostka": form.jednostka.data,
            "ilosc": form.ilosc.data,
            "cena": form.cena.data
            }
        BasicInvoiceGenerate(formdata)
        directory = 'static/'
        filename = 'tuto1.pdf'
        return send_from_directory(directory, filename)
    return render_template("create.html", form=form)

@views.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('views.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('views.home'))
    return render_template('login.html', title='Sign In', form=form)

@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@views.route('/sign_up', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('views.login'))
    return render_template('register.html', title='Rejestracja', form=form)