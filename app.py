from flask import Flask, render_template, request, redirect, session,jsonify
from flask.ext.hashing import Hashing
from flask.ext.user import login_required

import fileHandler

web = Flask(__name__)

hashing = Hashing(web)

WEB_IP = "0.0.0.0"
WEB_PORT = 5000

SALT = ""

web.secret_key ="""@t/"Iq^7y5cV>`\'<Rlv"""

globe = {}
globe["session"] = session



# TODO: Make less unsafe
@web.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@web.route("/")
def default():
    return redirect("/home")

@web.route("/home")
def home():
    return render_template("home.html")

@web.route("/about")
def about():
    return render_template("about.html")

@web.route("/register", methods = ["GET"])
def register():
    return render_template("register.html")

@web.route("/registerUser", methods = ["POST"])
def registerUser():
    user_login = loadUserLogin()
    rf = request.args
    username = rf["username"]
    password = rf["password"]
    if len(password) < 4:
        return "Password must be 4 or more letters"
    if username in user_login:
        return "User already exists"
    updateUserLogin(username,hashing.hash_value(password, salt=SALT))
    updateUserData(username, {"kills" : 0, "points" : 0})
    return "1"

@web.route("/login")
def login():
    return render_template("login.html")

@web.route("/loginCheck",methods = ["POST"])
def loginCheck():
    rf = request.args

    username = rf["username"].encode("ascii")
    password = rf["password"].encode("ascii")

    if confirmUser(username,password):
        session["username"] = username
        return "1"
    else:
        return "0"

@login_required
@web.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/")

@login_required
@web.route("/user", methods = ["POST"])
def userPage():
    return render_template("user.html")


@web.route("/updateData")
def updateUser():
    rf = request.args

    username = rf["username"].encode("ascii")
    password = rf["password"].encode("ascii")
    
    if confirmUser(username,password):
       user_data = loadUserData()
       user_dict = user_data[username]
       updateLenientRF(user_dict,rf,"kills")
       updateLenientRF(user_dict,rf,"points")
       updateUserData(username, user_dict)

def loadUserLogin():
    return fileHandler.readJSON("data/userLogin.json")

def loadUserData():
    return fileHandler.readJSON("data/userData.json")

def updateUserLogin(username,hashpass):
    user_login = loadUserLogin()
    user_login[username] = {"password": hashpass}
    fileHandler.writeJSON(user_login,"data/userLogin.json")

def updateUserData(username,data):
    user_data = loadUserData()
    user_data[username] = data
    fileHandler.writeJSON(user_data,"data/userData.json")

def confirmUser(username, password):
    user_login = loadUserLogin()
    if not username in user_login.keys():
        return False
    user = user_login[username]
    return hashing.check_value(user["password"],password,salt=SALT)


def updateLenientRF(di,rf,key):
    if key in rf:
        di[key] = rf[key].encode("ascii")

if __name__ == "__main__":
    web.debug = True
    web.run(host = WEB_IP,port = WEB_PORT)
    user_login = loadUserLogin()
