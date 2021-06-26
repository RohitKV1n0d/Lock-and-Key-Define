from flask import Flask, render_template

app = Flask(__name__,template_folder="templates")

@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("landing-page.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/rules.html')
def rules():
    return render_template("rules.html")

@app.route('/start.html')
def start():
    return render_template("start-page.html")

@app.route('/unlock.html')
def unlock():
    return render_template("unlock.html")
    

@app.route('/key1.html')
def round1():
    return render_template("round1.html")



@app.route('/key2.html')
def round2():
    return render_template("round2.html")

@app.route('/key3.html')
def round3():
    return render_template("round3.html")


@app.route('/crossword')
def crossword():
    return render_template("round5.html")


@app.route('/key5.html')
def round5():
    return render_template("round5-answer.html")







    