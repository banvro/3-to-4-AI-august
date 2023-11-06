from flask import Flask, session, make_response, request

app = Flask(__name__)
app.secret_key = "wihadksadskdbsakjd"


@app.route("/set")
def store():
    zx = make_response("set up cookies done")
    zx.set_cookie("myname", "this is my name")
    zx.set_cookie("age", "20")
    zx.set_cookie("number", "983264923")
    return zx

    # session["username"] = "Kriss moris"
    # return "data set"


@app.route("/get")
def show():
    zx = request.cookies.get("myname")
    myg = request.cookies.get("age")
    return zx + " " + myg
    # if "username" in session:
    #     zx = session.get("username")
    #     return f"User name is : {zx}"
    # else:
    #     return "please login first"

@app.route("/dlt")
def dlt():
    zx = make_response("cookies remove")
    zx.set_cookie("myname", " ", expires=0)
    return zx
    # session.pop("username")
    # return "session ended"

if __name__ == "__main__":
    app.run(debug = True)

# set session : session["key"] = "value"
# get session : session.get("key")
# dlt session : session.pop("key")
# clear session : session.clear()



# cookies:
# set cookies : zx.set_cookie("key", "value")
# get cookkies : request.cookies.get("key")
# dltcookies : my.set_cookie("key", " ", expire = 0)