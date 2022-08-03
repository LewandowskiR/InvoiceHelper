# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, send_from_directory, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Invoice
from .forms import LoginForm, BasicInvoiceForm, RegistrationForm
from .pdfgenerator import BasicInvoiceGenerate
from . import db, allowed_file
from werkzeug.utils import secure_filename
import os


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/create', methods=['GET', 'POST'])
def createInvoice():
    form = BasicInvoiceForm()
    if form.validate_on_submit():         
        #if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            basedir = os.path.abspath(os.path.dirname(__file__))
            imageloc = f'{basedir}/static/invoiceimg.png'            
            BasicInvoiceGenerate(request.form, imageloc) 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            imageloc = f'{basedir}/static/uploads/{filename}'
            file.save(imageloc)
            BasicInvoiceGenerate(request.form, imageloc)
            os.remove(imageloc)
        directory = 'static/'
        filename = 'invoice1.pdf'
        
        #Adding Invoice to the database
        
        if not current_user.is_anonymous:
            invoice = Invoice(
                numer_faktury=form.numer_faktury.data,
                sprzedawca = form.sprzedawca.data,
                nip_sprzedawcy = form.nip_sprzedawcy.data,
                nabywca = form.nabywca.data,
                nip_nabywcy=form.nip_nabywcy.data,
                creator = current_user
                )
            db.session.add(invoice)
            db.session.commit()
        
        return send_from_directory(directory, filename)
    print("not validated")
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

@views.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    invoices = Invoice.query.filter_by(user_id = current_user.id)
    return render_template('user.html', user=user, invoices=invoices)