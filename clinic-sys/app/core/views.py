from flask import render_template, request, redirect, session, flash, url_for
from main import db, app
from models.models import Admin,Person,Reports

@app.route('/')
def root():
    return 'Root Start'