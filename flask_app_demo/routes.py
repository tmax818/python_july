from flask import Flask, request, session

app = Flask(__name__)

app.secret_key = "whatever string I want"

@app.route('/')
def index():
    return "hello"

@app.route('/test')
def test():
    return '<form action="/post" method="post"><input type="text" name="data" ><input type="submit" value="submit">'

@app.route('/post', methods = ['post'])
def post():
    print(request)
    session['data'] = request.form['data']
    return f"<h1>{session['data']}</h1>"