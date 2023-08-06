from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add_to/dojos', methods=['POST'])
def add_dojo():
    print("request.form in add_dojo: ", request.form)
    data = {
        "dojo_name": request.form['dojo_name']
    }
    Dojo.save_dojo_to_db(data)
    return redirect("/dojos")

@app.route('/dojos')
def show_all_dojos():
    dojos = Dojo.get_all_dojos_in_db()
    return render_template('index.html',dojos=dojos)

@app.route('/view/dojo/<int:dojo_id>')
def show_one_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template('dojo.html', dojo = Dojo.get_one_dojo_in_db(data))

@app.route('/delete/dojo/<int:id>')
def delete_dojo(id):
    Dojo.delete_dojo_from_db(id)
    return redirect("/dojos")