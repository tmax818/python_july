from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.dojo import Dojo

# ! ////////  CREATE  //////////
# ! POST requires two routes:

# ! This one displays the form
@app.route('/dojo/new')
def new_dojo():
    return render_template('new_dojo.html')

# ! This one handles the data from the form
@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')

# ! ////////  READ or RETRIEVE  //////////
@app.route('/')
def dojo_index():
    dojos = Dojo.get_all()

    return render_template('index.html', dojos = dojos)

@app.route('/dojo/show/<int:id>')
def dojo_show(id):
    data = {'id': id}
    return render_template('show_dojo.html', dojo=Dojo.get_one_with_ninjas(data))

# ! //////// UPDATE  //////////
# ! POST requires two routes

# ! This one displays the form
@app.route('/dojo/edit/<int:id>')
def edit_dojo(id):
    data ={'id': id}
    return render_template('edit_dojo.html', dojo = Dojo.get_one(data))

# ! This one handles the data from the form
@app.route('/dojo/update', methods=['POST'])
def update_dojo():
    Dojo.update(request.form)
    return redirect('/')


# ! //// DELETE ////

@app.route('/dojo/destroy/<int:id>')
def destroy_dojo(id):
    data = {'id': id}
    Dojo.destroy(data)
    return redirect('/')