from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename
from model import predict
import xlrd
import pandas as pd
from users import login_data,registeration,get_data
from suggest import suggestions
app=Flask(__name__)
user=""

def getUser():
    return user

@app.route("/")
def home():
    return render_template("bootstrap-5.0.2-dist/home.html")

@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        image = request.files.get('imagefile', 'update-form')
        image = request.form["imagefile"]
        images = []
        images.append(image)
        out=predict(images)
        print(out)
        return render_template('bootstrap-5.0.2-dist/home.html',food = out[0],volume=str(out[1]),calorie=str(out[2]))

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("bootstrap-5.0.2-dist/login.html")

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        global user
        user=request.form.get("user")
        user1=user
        password=request.form.get("password")
        
        msg=login_data(user,password)
        print(user,password,msg)
        if(msg):
            if(user1):
                return render_template("bootstrap-5.0.2-dist/home1.html",user=user1)
            else:
                return render_template("bootstrap-5.0.2-dist/home1.html",user="")
        else:
            msg="Login Failed!! Wrong User Crendentials.Please try again."
            return render_template("bootstrap-5.0.2-dist/login.html",msg=msg)

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("bootstrap-5.0.2-dist/register.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    user=request.form.get("user")
    password=request.form.get("psw")
    cpass=request.form.get("cpsw")
    email=request.form.get("email")
    gender=request.form.get("gender")
    age=request.form.get("age")
    health_issues=request.form.get("health")
    result=registeration(user,password,cpass,email,gender,age,health_issues)
    if(result=="existed"):
        msg="User already existed!!"
    elif(result=="error"):
        msg="Something went wrong. Please try again!!"
    elif(result=="password"):
        msg="Your password and confirm password is different."
    else:
        return render_template("bootstrap-5.0.2-dist/login.html")
    return render_template("bootstrap-5.0.2-dist/register.html",msg=msg)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return render_template("bootstrap-5.0.2-dist/home.html")

@app.route("/home1", methods=['GET', 'POST'])
def home1():
    age,gender,health_issues=get_data(getUser())
    print(getUser())
    if request.method == "POST":
        image = request.files.get('imagefile', 'update-form')
        image = request.form["imagefile"]
        images = []
        images.append(image)
        out=predict(images)
        print(out)
        result=suggestions(age,gender,health_issues)
        print(user,result)
        return render_template("bootstrap-5.0.2-dist/home1.html",user=getUser(),food = out[0],volume=str(out[1]),calorie=str(out[2]),result=result)

if __name__=='__main__':
    app.run()