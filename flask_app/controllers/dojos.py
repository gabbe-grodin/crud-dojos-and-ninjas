from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def home():
    return redirect("/dojos")

# Invisible route
@app.route('/add_to/dojos', methods=['POST'])
def add_dojo():
    print("request.form in add_dojo: ", request.form)

    Dojo.create_dojo(request.form)
    return redirect("/dojos")

# Viewing form to add dojo and list of all dojos
@app.route('/dojos')
def show_all_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html',dojos=dojos)

# View of one dojo
@app.route('/view/dojo/<int:dojo_id>')
def show_one_dojo_with_ninjas(dojo_id):
    data = {
            "id": dojo_id,
            # "id": ['id'],
            "first_name": ['first_name'],
            "last_name": ['last_name'],
            "age": ['age']
    }

    dojo = Dojo.get_one_dojo_with_ninjas(data)
    print("REEEEEEZZZZZUUUUUUULLLLLLTZZZZ", data)
    if dojo:
        return render_template('dojo.html',dojo=dojo)
    else:
        return redirect("/dojos")

@app.route('/delete/dojo/<int:id>')
def delete_dojo(id):
    Dojo.delete_dojo_from_db(id)
    return redirect("/dojos")