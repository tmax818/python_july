from flask_app import app, render_template, redirect, request, session
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods = ['post'])
def register_user():
    # validate user info from form
    # hash password
    # create data dict to change password value to the hash created above.
    # save user to database
    # log user in
    # redirect to app page
    return redirect('/dashboard')

@app.route('/users/login', methods = ['post'])
def login_user():
    # query database for user email from form
    # use query to redirect if not found
    # check password in form against password hash in database
    # redirect if not found
    # log user in
    # redirect to app page
    return redirect('/dashboard')

@app.route('/users/show/<int:id>')
def show_user(id):
    # create user show page if necessary
    return render_template("show_user.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')