from flask_app import app, render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods = ['post'])
def register_user():
    print(request.form)
    # validate user info from form
    if not User.validate_user(request.form):
        return redirect('/')
    # hash password
    # create data dict to change password value to the hash created above.
    # save user to database
    # log user in
    # redirect to app page
    return redirect('/dashboard')