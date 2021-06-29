

import os
import re
import string
import datetime
#from . import keys

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

# app.config['SQLALCHEMY_DATABASE_URI'] = uri
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# if ENV == 'dev' :
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rkv#3117@localhost/user_data'

# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = ''
#     app.debug = False

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 







ENV = 'prod'

if ENV == 'dev' :
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../my_flask/user_database.db'
    app.config['SECRET_KEY'] = 'ajbdihswvkhbwfvjblanvljadn322rijfqp31'

else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    
SQLALCHEMY_TRACK_MODIFICATIONS = False



timeStamp =  str(datetime.datetime.now())


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'





class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique=True) 
    email = db.Column(db.String(50), unique=True ) 
    role = db.Column(db.String(10))
    password = db.Column(db.String(255))
    key1_time = db.Column(db.String(50))
     




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Username is required'),Length(min=4, max=15)])
    password = PasswordField('password', validators= [InputRequired(), Length(min=8, max=81, message=('8 letters!'))])
    remember = BooleanField('remember me')


class ResgisterForm(FlaskForm):
    email = StringField('email', validators = [InputRequired(), Email(), Length(max=50) ])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators= [InputRequired(), Length(min=8, max=81)])




#Admin
AdminUsername = 'Admin@user'
AdminPassword = 'Admin@user123'
def admin_status(Astatus):
    status = Astatus
    if status == 1:
        return True
    else:
        return False 
admin_status(0)
    


check_admin = User.query.filter_by(username='Admin@user').first()
if check_admin== None :
    admin_user = User(username=AdminUsername, email='crizal501@gmail.com',role='admin', password=AdminPassword)        
    db.session.add(admin_user)
    db.session.commit()








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
            # if check_password_hash(user.password, form.password.data):
            if form.username.data == AdminUsername: 
                login_user(user,AdminPassword)
                admin_status(1)
                if admin_status:
                    return 'admin page'
                else:
                    return 'somehting Woring'

            if user.password == form.password.data:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('start'))
        return '<h1>Invalid username or password</h1>'
        
    return render_template("login.html", form=form)

#######################################################################################################


@app.route('/register.html', methods=['GET', 'POST'])                                    #Registration
def register():
    form = ResgisterForm()
    
    if form.validate_on_submit():
       # hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data,role='player', password=form.password.data, key1_time=timeStamp)#hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
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










    