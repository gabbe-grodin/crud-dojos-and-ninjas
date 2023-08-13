from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import ninja, dojo



@app.route('/')
def index():
    return render_template("index.html")


# READ form
@app.route('/view/ninja/form')
def show_ninja_form():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('ninja.html', dojos = dojos)


# CREATE
@app.route('/add/ninja', methods=['POST'])
def add_one_ninja():
    ninja.Ninja.save_ninja_to_db(request.form)
    return redirect(f'/view/dojo/{request.form["dojo_id"]}')


# DELETE
@app.route('/delete/ninja/<ninja_id>/<dojo_id>')
def delete_ninja(ninja_id, dojo_id):
    print("Deleting Ninja with ID: ", ninja_id)
    ninja.Ninja.delete_ninja_by_id(ninja_id)
    # Dojo.get_one_dojo_with_ninjas(dojo_id)
    return redirect(f'/view/dojo/{dojo_id}')


# READ form
@app.route('/edit/ninja/<ninja_id>/form')
def show_update_ninja_form(ninja_id):
    print("Got through to edit route for updating ninja with ID of:", ninja_id)
    dojos = dojo.Dojo.get_all_dojos()
    print(dojos,"*"*20)
    ninja_object = ninja.Ninja.get_one_ninja_by_id(ninja_id)
    return render_template('update.html', ninja=ninja_object, dojos=dojos)
    # return render_template('update.html', ninja = Ninja.get_one_ninja_by_id(ninja_id))


# UPDATE
@app.route('/update/ninja/process', methods=['POST'])
def update_one_ninja():
    # print("Printing Ninja with ID: ", ninja_id)
    print("*"*20,request.form) # good practice to always do this on post methods
    ninja.Ninja.update_ninja_by_id(request.form)
    return redirect(f'/view/dojo/{request.form["dojo_id"]}')