from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/view/ninja/form')
def show_ninja_form():
    dojos = Dojo.get_all_dojos_in_db()
    return render_template('ninja.html', dojos = dojos)

@app.route('/add/ninja', methods=['POST'])
def add_one_ninja():
    data = {
            "dojo_id": request.form['dojo_id'],
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "age": request.form['age']
    }
    Ninja.save_ninja_to_db(data)
    return redirect('/view/dojo/1')

# @app.route('/edit/ninja')

# @app.route('/delete/ninja')

