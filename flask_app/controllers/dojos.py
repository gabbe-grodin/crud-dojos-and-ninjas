from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import dojo, ninja



@app.route('/')
def home():
    return redirect("/dojos")


# Invisible route
@app.route('/add_to/dojos', methods=['POST'])
def add_dojo():
    # print("request.form in add_dojo: ", request.form)
    dojo.Dojo.create_dojo(request.form)
    return redirect("/dojos")


# Viewing form to add dojo and list of all dojos
@app.route('/dojos')
def show_all_dojos():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('index.html',dojos=dojos)


# View of one dojo and its ninjas
@app.route('/view/dojo/<dojo_id>')
def show_one_dojo_with_ninjas(dojo_id):
    data = {
            "dojo_id": dojo_id,
            "first_name": ['first_name'],
            "last_name": ['last_name'],
            "age": ['age']}
    dojo_ninjas = dojo.Dojo.get_one_dojo_with_ninjas(data) # calling model query for conditional
    print("REEEEEEZZZZZUUUUUUULLLLLLTZZZZ", data)
    if dojo_ninjas:
        return render_template('dojo.html',dojo=dojo_ninjas)
    else:
        return redirect("/dojos")


@app.route('/delete/dojo/<int:id>')
def delete_dojo(id):
    dojo.Dojo.delete_dojo_from_db(id)
    return redirect("/dojos")