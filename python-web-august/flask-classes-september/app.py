from flask import Flask, render_template, request, redirect
import mysql.connector


conn = mysql.connector.connect(host = "localhost", user = "root", password = "1234", database = "test")

curser = conn.cursor()

# curser.execute("create table tblxyz(Name varchar(30), Phone_Number int, Email varchar(30), Message varchar(12));")







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
    curser.execute("select * from tblxyz;")
    zx = curser.fetchall()
    return render_template("home.html", data = zx)

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
    if request.method == "POST":
        usernmae = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        dec = request.form.get("msg")

        curser.execute(f"insert into tblxyz values('{usernmae}', {phone}, '{email}', '{dec}')")
        conn.commit()

    return redirect('contact-us')
        
    # return "save data"

if __name__ == "__main__":
    app.run(debug = True, port=7000)



