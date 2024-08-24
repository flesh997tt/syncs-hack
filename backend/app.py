from flask import Flask, render_template, request, redirect, url_for, flash, session
from backend import Backend


app = Flask(__name__, template_folder='../HTML', static_folder='../static')
backend = Backend('data.txt')
backend.parse_file()
app.secret_key = "HEY"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if backend.login_checker(username, password):
            session['username'] = username
            return redirect(url_for('friend_list'))
        return render_template("login.html")
    return render_template("login.html")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        print(name,username,password)
        if backend.add_user(name,username,password):
            session['username'] = username
            return redirect(url_for('home_page'))
        return render_template("sign_up.html")
    return render_template("sign_up.html")

@app.route("/friend_list")
def friend_list():
    username = session['username']
    me = backend.find_username(username)
    friend = me.online_friends()
    return render_template("friend_list.html", friend_list=friend)
    
@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.route("/profile_page", methods=["GET", "POST"])
def profile_page():
    if request.method == "POST":
        ics_link = request.form['ics']
        me = backend.find_username(username)
        username = me.change_ics(ics_link)
    username = session['username']
    return render_template("profile_page.html", username=username)

@app.route("/sign_out")
def sign_out():
    session.pop('username', default=None)

