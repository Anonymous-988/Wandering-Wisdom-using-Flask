from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__, template_folder="template")
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def callAbout():
    return render_template("about.html")

@app.route("/service")
def callService():
    return render_template("service.html")

@app.route("/product")
def callProduct():
    return render_template("product.html")

@app.route("/gallery")
def callGallery():
    return render_template("gallery.html")

@app.route("/feature")
def callFeature():
    return render_template("feature.html")

@app.route("/team")
def callTeam():
    return render_template("team.html")

@app.route("/testimonial")
def callTestimonial():
    return render_template("testimonial.html")

@app.route("/contact")
def callContact():
    return render_template("contact.html")

# if __name__ == "__main__":
#     app.run()