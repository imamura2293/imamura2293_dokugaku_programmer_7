

$　pip

$ sudo pip install Flask==0.11.1

$ pip install flask==0.11.1

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


app.run(port=8000)

$ pip freeze



$ pip uninstall Flask


