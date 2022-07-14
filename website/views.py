# -*- coding: utf-8 -*-
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '<h1>Strona Tytułowa</h1>'