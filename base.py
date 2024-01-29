from flask import Flask, render_template

app = Flask(__name__)



@app.route("/rent")
def rent():
    return render_template('rent.html')


@app.route("/mortgage")
def mortgage():
    return render_template('mortgage.html')


@app.route("/login")
def ad():
    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')



@app.route("/buy-home")
def buy():
    return render_template('buy-home.html')


@app.route("/agency")
def agency():
    return render_template('agency.html')


@app.route("/")
def login_page():
    return render_template('login.html')





app.run(host='0.0.0.0', debug=True)