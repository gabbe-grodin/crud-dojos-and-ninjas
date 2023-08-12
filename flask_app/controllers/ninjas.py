from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/view/ninja/form')
def show_ninja_form():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', dojos = dojos)

@app.route('/add/ninja', methods=['POST'])
def add_one_ninja():
    Ninja.save_ninja_to_db(request.form)
    return redirect(f'/view/dojo/{request.form["dojo_id"]}')

# @app.route('/edit/ninja')

# @app.route('/delete/ninja')

