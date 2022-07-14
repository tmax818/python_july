from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.ninja import Ninja

# ! ////////  CREATE  //////////
# ! POST requires two routes:

# ! This one displays the form
@app.route('/ninja/new')
def new_ninja():
    return render_template('new_ninja.html')

# ! This one handles the data from the form
@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')

# ! ////////  READ or RETRIEVE  //////////
@app.route('/ninjas')
def index():
    ninjas = Ninja.get_all()

    return render_template('index.html', ninjas = ninjas)

# ! //////// UPDATE  //////////
# ! POST requires two routes

# ! This one displays the form
@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data ={'id': id}
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

# ! This one handles the data from the form
@app.route('/ninja/update', methods=['POST'])
def update_ninja():
    Ninja.update(request.form)
    return redirect('/')


# ! //// DELETE ////

@app.route('/ninja/destroy/<int:id>')
def destroy_ninja(id):
    data = {'id': id}
    Ninja.destroy(data)
    return redirect('/')