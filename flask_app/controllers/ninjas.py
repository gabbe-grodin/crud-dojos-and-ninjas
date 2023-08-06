from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/add_one_to/ninjas', methods=['POST'])
# def add_ninja():
    