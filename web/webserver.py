from flask import Flask, render_template, url_for, request, redirect
from db import check_signup, view, write

app = Flask(__name__, static_folder="templates/styles")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/new_customer", methods=["POST", "GET"])
def new_customer():
    print('not epic test')
    username = request.form["username"]
    pw = request.form["pw"]
    print(f"Added '{username}' with password '{pw}'")
    check_dups = check_signup(username)
    if check_dups:
        return '<script>alert("Thar username is already taken.")</script>'
    
    write(username, pw)
    return redirect("/")

app.run(debug=True, port=2663)