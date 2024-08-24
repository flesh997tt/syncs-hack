from flask import Flask, render_template, request, redirect, url_for, flash, session
from backend import Backend

app = Flask(__name__)
backend = Backend('backend/data.txt')
app.secret_key = "HEY"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        attempt = request.form['username']
        if backend.login_checker(attempt):
            session['username'] = attempt
            return redirect(url_for('friend_list'))
        return render_template("HTML/login.html")
    return render_template("HTML/login.html")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        if not backend.add_user(name,username,password):
            session['username'] = username
            return redirect(url_for('home_page'))
        return render_template("HTML/sign_up.html")
    return render_template("HTML/sign_up.html")

@app.route("/friend_list")
def friend_list():
    username = session['username']
    me = backend.find_username(username)
    friend = me.online_friends()
    return render_template("HTML/friend_list.html", friend_list=friend)
    
@app.route("/home_page")
def home_page():
    return render_template("HTML/home_page.html")

@app.route("/profile_page", methods=["GET", "POST"])
def profile_page():
    if request.method == "POST":
        ics_link = request.form['ics']
        me = backend.find_username(username)
        username = me.change_ics(ics_link)
    username = session['username']
    return render_template("HTML/profile_page.html", username=username)

@app.route("/sign_out")
def sign_out():
    session.pop('username', default=None)

