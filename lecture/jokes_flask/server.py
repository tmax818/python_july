from flask import Flask, render_template
import requests
from pprint import pprint


app =Flask(__name__)

@app.route("/")
def index():
    data = requests.get("https://swapi.dev/api/people/1")
    pprint(data.json())
    return render_template('index.html', data = data.json())

if __name__ == "__main__":
    app.run(debug=True)