from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "welcom to my flask app..."

@app.route("/car/<int:id>")
def about(id):
    return f"this is my about page...{id}"

@app.route("/show")
def showpage():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)



