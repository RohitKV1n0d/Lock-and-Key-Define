

import os
import re
import string
import datetime


from flask import Flask, render_template, redirect, url_for, session, g , request


from flask_wtf import FlaskForm
from sqlalchemy.orm import backref
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators
from wtforms.validators import InputRequired, Email, Length

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
 
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView



key1 = 26
key2 = 21
key3 = 12
key4 = 54
key5 = 76
key6 = 43
key7 = 23
key8 = 54



ans_round1 = "answer"
ans_round2 = "answer"
ans_round3 = "answer"   #bonus roun
ans_round4 = "answer"
ans_round5 = ['0','0','0','0','0','0','0','0','0','0','0','0']
ans_round6 = "answer"
ans_round7 = "answer"
ans_round8 = "answer"






app = Flask(__name__,template_folder="templates")
app.secret_key = 'aasdaskhvahdcbjabdcoubqduoicb'


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




#http://127.0.0.1:5000/admin
#https://lockandkey-define.in/admin/


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



 


db = SQLAlchemy(app)





login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'





class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique=True) 
    email = db.Column(db.String(50), unique=True ) 
    role = db.Column(db.String(256))
    password = db.Column(db.String(256))
    reg_time = db.Column(db.String(256))
    key1= db.Column(db.String(20))
    key2= db.Column(db.String(20))
    key3= db.Column(db.String(20))
    key4= db.Column(db.String(20))
    key5= db.Column(db.String(20))
    key6= db.Column(db.String(20))
    key7= db.Column(db.String(20))
    key8= db.Column(db.String(20))
    unlcok_time = db.Column(db.String(256))
    



     




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Username is required'),Length(min=4, max=15,message='must be min 4 letters')])
    password = PasswordField('password', validators= [InputRequired(), Length(min=8, max=81, message=('8 letters!'))])
    remember = BooleanField('remember me')


class ResgisterForm(FlaskForm):
    email = StringField('email', validators = [InputRequired(), Email(), Length(max=50) ])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators= [InputRequired(), Length(min=8, max=81)])

class GetAnswer(FlaskForm):
    answer = StringField('answer', validators=[InputRequired()] )

class round5_ans(FlaskForm):
    a1 = StringField('key1', validators=[InputRequired()] )
    a2 = StringField('key2', validators=[InputRequired()] )
    a3 = StringField('key3', validators=[InputRequired()] )
    a4 = StringField('key4', validators=[InputRequired()] )
    a5 = StringField('key5', validators=[InputRequired()] )
    a6 = StringField('key6', validators=[InputRequired()] )
    a7 = StringField('key7', validators=[InputRequired()] )
    a8 = StringField('key8', validators=[InputRequired()] )
    a9 = StringField('key9', validators=[InputRequired()] )
    a10 = StringField('key10', validators=[InputRequired()] )
    a11 = StringField('key11', validators=[InputRequired()] )
    a12 = StringField('key12', validators=[InputRequired()] )

    



class MyModelView(ModelView):
    def is_accessible(self):
        # if g.user.role == 'admin':
        #     return  True
        # else:
        #     return Fal
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(redirect(url_for('login')))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if g.user.role == 'admin':
            return  True
        else:
            return False
    
    



admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db.session))

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




@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()  
        g.user = user 









@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("landing-page.html")

@app.route('/login.html', methods=['GET', 'POST'])                                   #Login
def login():   
    form = LoginForm()
    if form.validate_on_submit():
        session.pop('user_id',None)
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # if check_password_hash(user.password, form.password.data):
            
            # if form.username.data == AdminUsername:
            #     session['user_id'] = user.id 
            #     login_user(user,AdminPassword)
            #     admin_status(1)
            #     if admin_status:
            #         return redirect(redirect(url_for('start')))
            #     else:
            #         return 'Something Working'

            if user.password == form.password.data:
                session['user_id'] = user.id
                login_user(user, remember=form.remember.data)
                return redirect(url_for('start'))
        return '<h1>Invalid username or password</h1>'
        
    return render_template("login.html", form=form)



@app.route('/register.html', methods=['GET', 'POST'])                                    #Registration
def register():
    form = ResgisterForm()
    
    if form.validate_on_submit():
       # hashed_password = generate_password_hash(form.password.data, method='sha256')
        time =str(datetime.datetime.now())
        new_user = User(username=form.username.data, email=form.email.data,role='player', password=form.password.data, reg_time= time)#hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)



#######################################################################################################




@app.route('/rules.html')
def rules():
    return render_template("rules.html")

@app.route('/start.html')
@login_required
def start():
    return render_template("start-page.html")

@app.route('/unlock')
@login_required
def unlock():
    return render_template("unlock.html")
    

@app.route('/key1.html', methods=['GET', 'POST'])                           #######    round 1
@login_required
def round1():
    nextKey = key1
    form = GetAnswer()
    if form.validate_on_submit():
        user = User.query.filter_by(id = g.user.id).first()
        if form.answer.data == ans_round1:
            user.key1 = '1'                   
            db.session.add(user)
            db.session.commit()
    return render_template("round1.html" , form=form, nextKey=nextKey)



@app.route('/key2.html', methods=['GET', 'POST'])                                                     #######    round 2
@login_required
def round2():
    if g.user.key1 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = key2
        form = GetAnswer()
        if form.validate_on_submit():
            user = User.query.filter_by(id = g.user.id).first()
            if form.answer.data == ans_round2:
                user.key2 = '1'                   
                db.session.add(user)
                db.session.commit()
        return render_template("round2.html", form=form ,nextKey=nextKey)



@app.route('/key3.html')                                                                                  #######    round 3
@login_required
def round3():
    if g.user.key2 != '1':
        return "Finish the last round you sneaky KID!"

    return render_template("round3.html")


@app.route('/key4.html',  methods=['GET', 'POST'])                                                           #######    round 4
@login_required
def round4():
    if g.user.key2 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = key4
        form = GetAnswer()
        if form.validate_on_submit():
            user = User.query.filter_by(id = g.user.id).first()
            if form.answer.data == ans_round4:
                user.key4 = '1'                   
                db.session.add(user)
                db.session.commit()

        return render_template("round4.html", form=form ,nextKey=nextKey)





@app.route('/crossword')                                                                                   #######    round 5
@login_required
def crossword():
    if g.user.key4 != '1':
        return "Finish the last round you sneaky KID!"

    return render_template("round5.html")





@app.route('/key5.html',  methods=['GET', 'POST'])                                             #######    round 5 ANSWER
@login_required
def round5():
    if g.user.key4 != '1':
        return "Finish the last round you sneaky KID!"
    else:   
        nextKey = key5
        form = round5_ans()
        if form.validate_on_submit():
            user = User.query.filter_by(id = g.user.id).first()
            if form.a1.data == str(ans_round5[0]):
                if form.a2.data == str(ans_round5[1]):
                    if form.a3.data == str(ans_round5[2]):
                        if form.a4.data == str(ans_round5[3]):
                            if form.a5.data == str(ans_round5[4]):
                                if form.a6.data == str(ans_round5[5]):
                                    if form.a7.data == str(ans_round5[6]):
                                        if form.a8.data == str(ans_round5[7]):
                                            if form.a9.data == str(ans_round5[8]):
                                                if form.a10.data == str(ans_round5[9]):
                                                    if form.a11.data == str(ans_round5[10]):
                                                        if form.a12.data == str(ans_round5[11]):
                                                            user.key5 = '1'                   
                                                            db.session.add(user)
                                                            db.session.commit()

            

            
                
        
        return render_template("round5-answer.html", form=form ,nextKey=nextKey)


@app.route('/key6.html', methods=['GET', 'POST'])                                                                                     #######    round 6
@login_required
def round6():
    if g.user.key5 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = key6
        form = GetAnswer()  
        if form.validate_on_submit():
            user = User.query.filter_by(id = g.user.id).first()
            if form.answer.data == ans_round6:
                user.key6 = '1'                   
                db.session.add(user)
                db.session.commit()    
        return render_template("round6.html",  form=form ,nextKey=nextKey)


@app.route('/key7.html')                                                                                     #######    round 7
@login_required
def round7():
    return render_template("round7.html")




@app.route('/key8.html')                                                                                     #######    round 8
@login_required
def round8():
    return render_template("round8.html")






@app.route('/logout')
@login_required
def logout():
    
    logout_user()
    return redirect(url_for('welcome'))




if __name__ == '__mainn__' :
    app.run()










    