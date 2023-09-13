from flask import Flask, render_template
app = Flask(__name__)

@app.route("/car")
def home():
    return "welcom to my flask app..."

@app.route("/car/<int:id>")
def about(id):
    return f"this is my about page...{id}"

@app.route("/show")
def showpage():
    return render_template("home.html")


@app.route("/myfrom")
def showfome():
    return render_template("myfrom.html")



@app.route("/")
def home1():
    return render_template("home.html")

@app.route("/about-us")
def about1():
    return render_template("about.html")

@app.route("/contact-us")
def contact1():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/savedata", methods = ["post", ])
def save():
    return "save data"

if __name__ == "__main__":
    app.run(debug = True)



