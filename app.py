

import os
import re

from flask import Flask, render_template, redirect, url_for


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators
from wtforms.validators import InputRequired, Email, Length

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash


from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user




app = Flask(__name__,template_folder="templates")


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../my_flask/user_database.db'
# app.config['SQLALCHEMY_BINDS'] = {'Progress' : 'sqlite:///../my_flask/progress_database.db' }

# uri = os.getenv("postgres://zpcdgfxgkfizaa:dc91ac3d675ca76fb01b3e66b264b04cfa4628eab97ff13379bf971e5d886120@ec2-54-224-120-186.compute-1.amazonaws.com:5432/d5lj8l6oardsvc")  # or other relevant config var
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)

# app.config['SQLALCHEMY_DATABASE_URI'] = uri
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# ENV = 'dev'

# if ENV == 'dev' :
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rkv#3117@localhost/user_data'

# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = ''
#     app.debug = False

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 




SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY








db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique=True) 
    email = db.Column(db.String(50), unique=True ) 
    password = db.Column(db.String(80)) 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
# class UserProgress(db.Model):
#     __bind_key__ = 'Progress'
#     id = db.Column(db.Integer, primary_key = True)
#     key1 = db.Column(db.Boolean)
#     key1_time = db.Column(db.Time)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Username is required'),Length(min=4, max=15)])
    password = PasswordField('password', validators= [InputRequired(), Length(min=8, max=80, message=('8 letters!'))])
    remember = BooleanField('remember me')


class ResgisterForm(FlaskForm):
    email = StringField('email', validators = [InputRequired(), Email(), Length(max=50) ])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators= [InputRequired(), Length(min=8, max=80)])







@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("landing-page.html")

@app.route('/login.html', methods=['GET', 'POST'])                                   #Login
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('start'))
        return '<h1>Invalid username or password</h1>'
        
    return render_template("login.html", form=form)

#######################################################################################################


@app.route('/register.html', methods=['GET', 'POST'])                                    #Registration
def register():
    form = ResgisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
    return render_template("register.html", form=form)







@app.route('/rules.html')
def rules():
    return render_template("rules.html")

@app.route('/start.html')
@login_required
def start():
    return render_template("start-page.html")

@app.route('/unlock.html')
@login_required
def unlock():
    return render_template("unlock.html")
    

@app.route('/key1.html')
@login_required
def round1():
    return render_template("round1.html")



@app.route('/key2.html')
@login_required
def round2():
    return render_template("round2.html")

@app.route('/key3.html')
@login_required
def round3():
    return render_template("round3.html")


@app.route('/crossword')
@login_required
def crossword():
    return render_template("round5.html")


@app.route('/key5.html')
@login_required
def round5():
    return render_template("round5-answer.html")








@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome'))




if __name__ == '__mainn__' :
    app.run()










    