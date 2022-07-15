from flask_app import app, render_template, redirect, request, bcrypt, session
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
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # create data dict to change password value to the hash created above.
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password":pw_hash
    }
    # save user to database
    user_id = User.save(data)
    # log user in
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
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