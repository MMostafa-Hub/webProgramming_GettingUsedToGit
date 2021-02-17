from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)


# @app.route("/<string:name>")
# def index(name):
#     headline = name
#     return render_template("indexPY.html", headline=headline)


# @app.route('/<string:x>')
# def hello(x):
#     return f"<h1>Hello , {x} !!</h1>"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["POST", "GET"])
def index():
    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("indexForm.html", notes=session["notes"])

# @app.route("/more")
# def more():
#     return render_template("morePY.html")


# @app.route("/hello", methods=["POST"])
# def hello():
#     name = request.form.get("name")
#     return render_template("hello.html", name=name)
