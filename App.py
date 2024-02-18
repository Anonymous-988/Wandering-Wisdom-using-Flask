from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__, template_folder="template")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello_person(name):
    return f"<p>Hello, {escape(name)}!</p>"

@app.route("/app")
def index():
    return render_template("index.html")

# if __name__ == "__main__":
#     app.run()