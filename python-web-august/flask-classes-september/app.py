from flask import Flask, render_template, request, redirect
import mysql.connector
import os

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
        print("ehyyyyyyyyyyyyyy")
        usernmae = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        dec = request.form.get("msg")
        myimg = request.files.get("image")
        if myimg:
            myimg.save(os.path.join("static/images/", myimg.filename))
            img = os.path.join("static/images/", myimg.filename)

        curser.execute(f"insert into tblxyz values('{usernmae}', {phone}, '{email}', '{dec}', '{img}')")
        conn.commit()

    return redirect('contact-us')
        
    # return "save data"



@app.route("/delete/<name>", methods = ["post",])
def deletethis(name):
    curser.execute(f"delete from tblxyz where Name = '{name}'")
    return redirect("/")


@app.route("/update/<name>", methods = ["post", ])
def updateshowthis(name):
    curser.execute(f"select * from tblxyz where Name = '{name}';")
    data = curser.fetchall()
    return render_template("updatedata.html", mydata = data)
 
@app.route("/update-this/<name>", methods = ["post", ])
def updatethis(name):
    if request.method == "POST":
        usernmae = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        dec = request.form.get("msg")

        curser.execute(f"update tblxyz set Name = '{usernmae}',Email='{email}',Message='{dec}' where Name = '{name}' ; ")
        conn.commit()   
        return redirect("/") 
    return f"the name is {name}"




if __name__ == "__main__":
    app.run(debug = True, port=7000)



