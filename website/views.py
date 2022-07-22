# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, send_from_directory, request
from .forms import LoginForm, BasicInvoiceForm
from .pdfgenerator import BasicInvoiceGenerate


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
        #BasicInvoiceGenerate()
        directory = 'static/'
        filename = 'tuto1.pdf'
        return send_from_directory(directory, filename)
    return render_template("create.html", form=form)