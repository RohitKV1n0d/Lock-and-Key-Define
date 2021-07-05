

import os
import re
import string
import datetime

# import xlrd

from flask import Flask, render_template, redirect, url_for, session, g , request , jsonify


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

import temp_data

# import jyserver.Flask as jsf










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


ENV = 'dev'

if ENV == 'dev' :
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../my_flask/user_database.db'
    app.config['SECRET_KEY'] = 'ajbdihswvkhbwfvjblanvljadn322rijfqp31'

else:
    app.debug = False
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
    unlock = db.Column(db.String(256))
    key1= db.Column(db.String(256))
    key2= db.Column(db.String(256))
    key3= db.Column(db.String(256))
    key4= db.Column(db.String(256))
    key5= db.Column(db.String(256))
    key6= db.Column(db.String(256))
    key7= db.Column(db.String(256))
    key8= db.Column(db.String(256))
    key9= db.Column(db.String(256))

    unlcok_time = db.Column(db.String(256))
    
    hints = db.Column(db.String(256))

    hint1 = db.Column(db.String(256))
    time1 = db.Column(db.String(256))

    hint2 = db.Column(db.String(256))
    hint3 = db.Column(db.String(256))
    hint4 = db.Column(db.String(256))
    hint5 = db.Column(db.String(256))
    hint6 = db.Column(db.String(256))
    hint7 = db.Column(db.String(256))
    hint8 = db.Column(db.String(256))

    r1h1 = db.Column(db.String(256))
    r1h2 = db.Column(db.String(256))
    r1h3 = db.Column(db.String(256))

    r2h1 = db.Column(db.String(256))
    r2h2 = db.Column(db.String(256))
    r2h3 = db.Column(db.String(256))
    
    r3h1 = db.Column(db.String(256))
    r3h2 = db.Column(db.String(256))
    r3h3 = db.Column(db.String(256))

    r4h1 = db.Column(db.String(256))
    r4h2 = db.Column(db.String(256))
    r4h3 = db.Column(db.String(256))

    r5h1 = db.Column(db.String(256))
    r5h2 = db.Column(db.String(256))
    r5h3 = db.Column(db.String(256))

    r6h1 = db.Column(db.String(256))
    r6h2 = db.Column(db.String(256))
    r6h3 = db.Column(db.String(256))

    r7h1 = db.Column(db.String(256))
    r7h2 = db.Column(db.String(256))
    r7h3 = db.Column(db.String(256))

    r8h1 = db.Column(db.String(256))
    r8h2 = db.Column(db.String(256))
    r8h3 = db.Column(db.String(256))

    r9h1 = db.Column(db.String(256))
    r9h2 = db.Column(db.String(256))
    r9h3 = db.Column(db.String(256))
    



    
    
    
    


    



     




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

class round8_ans(FlaskForm):
    r1 = StringField('rkey1', validators=[InputRequired()] )
    r2 = StringField('rkey2', validators=[InputRequired()] )
    r3 = StringField('rkey3', validators=[InputRequired()] )
    r4 = StringField('rkey4', validators=[InputRequired()] )
    r5 = StringField('rkey5', validators=[InputRequired()] )
    r6 = StringField('rkey6', validators=[InputRequired()] )


class unlock(FlaskForm):
    key_1 = StringField('key_1', validators=[InputRequired()] )
    key_2 = StringField('key_2', validators=[InputRequired()] )
    key_3 = StringField('key_3', validators=[InputRequired()] )
    key_4 = StringField('key_4', validators=[InputRequired()] )
    key_5 = StringField('key_5', validators=[InputRequired()] )
    key_6 = StringField('key_6', validators=[InputRequired()] )
    key_7 = StringField('key_7', validators=[InputRequired()] )
    key_8 = StringField('key_8', validators=[InputRequired()] )


    



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
    admin_user = User(username=AdminUsername, email='crizal501@gmail.com',role='admin', password=AdminPassword,hints=5,
                         r1h1=temp_data.r1_hint1, r1h2=temp_data.r1_hint2, r1h3=temp_data.r1_hint3,
                         r2h1=temp_data.r2_hint1, r2h2=temp_data.r2_hint2, r2h3=temp_data.r2_hint3,
                         r3h1=temp_data.r3_hint1, r3h2=temp_data.r3_hint2, r3h3=temp_data.r3_hint3,
                         r4h1=temp_data.r4_hint1, r4h2=temp_data.r4_hint2, r4h3=temp_data.r4_hint3,
                         r5h1=temp_data.r5_hint1, r5h2=temp_data.r5_hint2, r5h3=temp_data.r5_hint3,
                         r6h1=temp_data.r6_hint1, r6h2=temp_data.r6_hint2, r6h3=temp_data.r6_hint3,
                         r7h1=temp_data.r7_hint1, r7h2=temp_data.r7_hint2, r7h3=temp_data.r7_hint3,
                         r8h1=temp_data.r8_hint1, r8h2=temp_data.r8_hint2, r8h3=temp_data.r8_hint3,
                         r9h1=temp_data.r9_hint1, r9h2=temp_data.r9_hint2, r9h3=temp_data.r9_hint3)              
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
    return render_template("ammu_landing-page.html")

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
        new_user = User(username=form.username.data, email=form.email.data,role='player', password=form.password.data, hints=5,
                         r1h1=temp_data.r1_hint1, r1h2=temp_data.r1_hint2, r1h3=temp_data.r1_hint3,
                         r2h1=temp_data.r2_hint1, r2h2=temp_data.r2_hint2, r2h3=temp_data.r2_hint3,
                         r3h1=temp_data.r3_hint1, r3h2=temp_data.r3_hint2, r3h3=temp_data.r3_hint3,
                         r4h1=temp_data.r4_hint1, r4h2=temp_data.r4_hint2, r4h3=temp_data.r4_hint3,
                         r5h1=temp_data.r5_hint1, r5h2=temp_data.r5_hint2, r5h3=temp_data.r5_hint3,
                         r6h1=temp_data.r6_hint1, r6h2=temp_data.r6_hint2, r6h3=temp_data.r6_hint3,
                         r7h1=temp_data.r7_hint1, r7h2=temp_data.r7_hint2, r7h3=temp_data.r7_hint3,
                         r8h1=temp_data.r8_hint1, r8h2=temp_data.r8_hint2, r8h3=temp_data.r8_hint3,
                         r9h1=temp_data.r9_hint1, r9h2=temp_data.r9_hint2, r9h3=temp_data.r9_hint3)#hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)







#######################################################################################################

hinttimer = 10000



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
    if g.user.role != 'admin':
        return render_template("early_vistors.html")
    else:
        user = User.query.filter_by(id = g.user.id).first()
        user.unlock = '1'                   
        db.session.add(user)
        db.session.commit()
        
        return render_template("unlock.html")


@app.route('/key1.html', methods=['GET', 'POST'])                           #######    round 1
@login_required
def round1():
    nextKey = temp_data.key1
    form = GetAnswer()
    user = User.query.filter_by(id = g.user.id).first()
    
    
    if form.validate_on_submit():
        if form.answer.data == temp_data.ans_round1:
            user.key1 = '1'                   
            db.session.add(user)
            db.session.commit()
    elif request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON 
        tempdata = request.get_json()
        HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
        if HINT[0] == None:
            user.hint1 = tempdata['hint'] 
            #user.time1 = tempdata['time']
        elif HINT[1] == None:
            user.hint2 = tempdata['hint']
            #user.time2 = tempdata['time']
        elif HINT[2] == None:
            user.hint3 = tempdata['hint']
            #user.time3 = tempdata['time']
        elif HINT[3] == None:
            user.hint4 = tempdata['hint']
            #user.time4 = tempdata['time']
        elif HINT[4] == None:
            user.hint5 = tempdata['hint']
            #user.time5 = tempdata['time']
        elif HINT[5] == None:
            user.hint6 = tempdata['hint']
            #user.time6 = tempdata['time']
        elif HINT[6] == None:
            user.hint7 = tempdata['hint']
            #user.time7 = tempdata['time']
        
        
        
        
 
            
        user.time1 = tempdata['time']
        user.hints =   int(g.user.hints) - 1                 
        db.session.add(user)
        db.session.commit()
        return 'OK', 200
    return render_template("round1.html" , form=form, nextKey=nextKey, hinttimer=hinttimer)










@app.route('/key2.html',  methods=['GET', 'POST'])                                                            #######    round 2
@login_required
def round2():
    if g.user.key1 != '1':
        return "Finish the last round you sneaky KID!"
    else:   
        nextKey = temp_data.key2    
        form = round8_ans()
        user = User.query.filter_by(id = g.user.id).first()
        if form.validate_on_submit():
            if form.r1.data == str(temp_data.ans_round2[0]):
                if form.r2.data == str(temp_data.ans_round2[1]):
                    if form.r3.data == str(temp_data.ans_round2[2]):
                        if form.r4.data == str(temp_data.ans_round2[3]):
                            if form.r5.data == str(temp_data.ans_round2[4]):
                                if form.r6.data == str(temp_data.ans_round2[5]):
                                    user.key2 = '1'                   
                                    db.session.add(user)
                                    db.session.commit()
        elif request.method == 'POST':
            print('Incoming..')
            print(request.get_json())  # parse as JSON 
            tempdata = request.get_json()
            HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
            if HINT[0] == None:
                user.hint1 = tempdata['hint'] 
                #user.time1 = tempdata['time']
            elif HINT[1] == None:
                user.hint2 = tempdata['hint']
                #user.time2 = tempdata['time']
            elif HINT[2] == None:
                user.hint3 = tempdata['hint']
                #user.time3 = tempdata['time']
            elif HINT[3] == None:
                user.hint4 = tempdata['hint']
                #user.time4 = tempdata['time']
            elif HINT[4] == None:
                user.hint5 = tempdata['hint']
                #user.time5 = tempdata['time']
            elif HINT[5] == None:
                user.hint6 = tempdata['hint']
                #user.time6 = tempdata['time']
            elif HINT[6] == None:
                user.hint7 = tempdata['hint']
                #user.time7 = tempdata['time']
   
            user.time1 = tempdata['time']
            user.hints =   int(g.user.hints) - 1                 
            db.session.add(user)
            db.session.commit()
            return 'OK', 200  
        
        return render_template("round2.html", form=form ,nextKey=nextKey,hinttimer=hinttimer)
    





@app.route('/key3.html')                                                                                  #######    round 3
@login_required
def round3():
    if g.user.key2 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        user = User.query.filter_by(id = g.user.id).first()
        user.key3 = '1'                   
        db.session.add(user)
        db.session.commit()

        return render_template("round3.html")


@app.route('/key4.html',  methods=['GET', 'POST'])                                                           #######    round 4
@login_required
def round4():
    if g.user.key2 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = temp_data.key4
        form = GetAnswer()
        user = User.query.filter_by(id = g.user.id).first()
        if form.validate_on_submit():           
            if form.answer.data == temp_data.ans_round4:
                user.key4 = '1'                   
                db.session.add(user)
                db.session.commit()
        elif request.method == 'POST':
            print('Incoming..')
            print(request.get_json())  # parse as JSON 
            tempdata = request.get_json()
            HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
            if HINT[0] == None:
                user.hint1 = tempdata['hint'] 
                #user.time1 = tempdata['time']
            elif HINT[1] == None:
                user.hint2 = tempdata['hint']
                #user.time2 = tempdata['time']
            elif HINT[2] == None:
                user.hint3 = tempdata['hint']
                #user.time3 = tempdata['time']
            elif HINT[3] == None:
                user.hint4 = tempdata['hint']
                #user.time4 = tempdata['time']
            elif HINT[4] == None:
                user.hint5 = tempdata['hint']
                #user.time5 = tempdata['time']
            elif HINT[5] == None:
                user.hint6 = tempdata['hint']
                #user.time6 = tempdata['time']
            elif HINT[6] == None:
                user.hint7 = tempdata['hint']
                #user.time7 = tempdata['time']

                
            user.time1 = tempdata['time']
            user.hints =   int(g.user.hints) - 1                 
            db.session.add(user)
            db.session.commit()
            return 'OK', 200

        return render_template("round4.html", form=form ,nextKey=nextKey,hinttimer=hinttimer)





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
        nextKey = temp_data.key5
        form = round5_ans()
        user = User.query.filter_by(id = g.user.id).first()
        if form.validate_on_submit():
            if form.a1.data == str(temp_data.ans_round5[0]):
                if form.a2.data == str(temp_data.ans_round5[1]):
                    if form.a3.data == str(temp_data.ans_round5[2]):
                        if form.a4.data == str(temp_data.ans_round5[3]):
                            if form.a5.data == str(temp_data.ans_round5[4]):
                                if form.a6.data == str(temp_data.ans_round5[5]):
                                    if form.a7.data == str(temp_data.ans_round5[6]):
                                        if form.a8.data == str(temp_data.ans_round5[7]):
                                            if form.a9.data == str(temp_data.ans_round5[8]):
                                                if form.a10.data == str(temp_data.ans_round5[9]):
                                                    if form.a11.data == str(temp_data.ans_round5[10]):
                                                        if form.a12.data == str(temp_data.ans_round5[11]):
                                                            user.key5 = '1'                   
                                                            db.session.add(user)
                                                            db.session.commit()
        elif request.method == 'POST':
            print('Incoming..')
            print(request.get_json())  # parse as JSON 
            tempdata = request.get_json()
            HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
            if HINT[0] == None:
                user.hint1 = tempdata['hint'] 
                #user.time1 = tempdata['time']
            elif HINT[1] == None:
                user.hint2 = tempdata['hint']
                #user.time2 = tempdata['time']
            elif HINT[2] == None:
                user.hint3 = tempdata['hint']
                #user.time3 = tempdata['time']
            elif HINT[3] == None:
                user.hint4 = tempdata['hint']
                #user.time4 = tempdata['time']
            elif HINT[4] == None:
                user.hint5 = tempdata['hint']
                #user.time5 = tempdata['time']
            elif HINT[5] == None:
                user.hint6 = tempdata['hint']
                #user.time6 = tempdata['time']
            elif HINT[6] == None:
                user.hint7 = tempdata['hint']
                #user.time7 = tempdata['time']

                
            user.time1 = tempdata['time']
            user.hints =   int(g.user.hints) - 1                 
            db.session.add(user)
            db.session.commit()
            return 'OK', 200  
        
        return render_template("round5-answer.html", form=form ,nextKey=nextKey,hinttimer=hinttimer)


@app.route('/key6.html', methods=['GET', 'POST'])                                        #######    round 6
@login_required
def round6():
    if g.user.key5 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = temp_data.key6
        form = GetAnswer()  
        user = User.query.filter_by(id = g.user.id).first()
        if form.validate_on_submit():         
            if form.answer.data == temp_data.ans_round6:
                user.key6 = '1'                   
                db.session.add(user)
                db.session.commit() 
        elif request.method == 'POST':
            print('Incoming..')
            print(request.get_json())  # parse as JSON 
            tempdata = request.get_json()
            HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
            if HINT[0] == None:
                user.hint1 = tempdata['hint'] 
                #user.time1 = tempdata['time']
            elif HINT[1] == None:
                user.hint2 = tempdata['hint']
                #user.time2 = tempdata['time']
            elif HINT[2] == None:
                user.hint3 = tempdata['hint']
                #user.time3 = tempdata['time']
            elif HINT[3] == None:
                user.hint4 = tempdata['hint']
                #user.time4 = tempdata['time']
            elif HINT[4] == None:
                user.hint5 = tempdata['hint']
                #user.time5 = tempdata['time']
            elif HINT[5] == None:
                user.hint6 = tempdata['hint']
                #user.time6 = tempdata['time']
            elif HINT[6] == None:
                user.hint7 = tempdata['hint']
                #user.time7 = tempdata['time']

                
            user.time1 = tempdata['time']
            user.hints =   int(g.user.hints) - 1                 
            db.session.add(user)
            db.session.commit()
            return 'OK', 200    
        return render_template("round6.html",  form=form ,nextKey=nextKey,hinttimer=hinttimer)


@app.route('/key7.html', methods=['GET', 'POST'])                                          #######    round 7
@login_required
def round7():
    if g.user.key6 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = temp_data.key7
        form = GetAnswer()
        user = User.query.filter_by(id = g.user.id).first()
        if form.validate_on_submit():           
            if form.answer.data == temp_data.ans_round7:
                user.key7 = '1'                   
                db.session.add(user)
                db.session.commit()
        elif request.method == 'POST':
            print('Incoming..')
            print(request.get_json())  # parse as JSON 
            tempdata = request.get_json()
            HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
            if HINT[0] == None:
                user.hint1 = tempdata['hint'] 
                #user.time1 = tempdata['time']
            elif HINT[1] == None:
                user.hint2 = tempdata['hint']
                #user.time2 = tempdata['time']
            elif HINT[2] == None:
                user.hint3 = tempdata['hint']
                #user.time3 = tempdata['time']
            elif HINT[3] == None:
                user.hint4 = tempdata['hint']
                #user.time4 = tempdata['time']
            elif HINT[4] == None:
                user.hint5 = tempdata['hint']
                #user.time5 = tempdata['time']
            elif HINT[5] == None:
                user.hint6 = tempdata['hint']
                #user.time6 = tempdata['time']
            elif HINT[6] == None:
                user.hint7 = tempdata['hint']
                #user.time7 = tempdata['time']

                
            user.time1 = tempdata['time']
            user.hints =   int(g.user.hints) - 1                 
            db.session.add(user)
            db.session.commit()
            return 'OK', 200

        return render_template("round7.html", form=form ,nextKey=nextKey,hinttimer=hinttimer)




@app.route('/key8.html', methods=['GET', 'POST'])                      #######    round 8
@login_required
def round8():
    if g.user.key7 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = temp_data.key8
        form = GetAnswer()
        user = User.query.filter_by(id = g.user.id).first()
        if form.validate_on_submit():           
            if form.answer.data == temp_data.ans_round8:
                user.key8 = '1'                   
                db.session.add(user)
                db.session.commit()
        elif request.method == 'POST':
            print('Incoming..')
            print(request.get_json())  # parse as JSON 
            tempdata = request.get_json()
            HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
            if HINT[0] == None:
                user.hint1 = tempdata['hint'] 
                #user.time1 = tempdata['time']
            elif HINT[1] == None:
                user.hint2 = tempdata['hint']
                #user.time2 = tempdata['time']
            elif HINT[2] == None:
                user.hint3 = tempdata['hint']
                #user.time3 = tempdata['time']
            elif HINT[3] == None:
                user.hint4 = tempdata['hint']
                #user.time4 = tempdata['time']
            elif HINT[4] == None:
                user.hint5 = tempdata['hint']
                #user.time5 = tempdata['time']
            elif HINT[5] == None:
                user.hint6 = tempdata['hint']
                #user.time6 = tempdata['time']
            elif HINT[6] == None:
                user.hint7 = tempdata['hint']
                #user.time7 = tempdata['time']

                
            user.time1 = tempdata['time']
            user.hints =   int(g.user.hints) - 1                 
            db.session.add(user)
            db.session.commit()
            return 'OK', 200

        return render_template("scavenger.html", form=form ,nextKey=nextKey,hinttimer=hinttimer)
    





@app.route('/key9.html', methods=['GET', 'POST'])                                                     #######    round 9
@login_required
def round9():
    if g.user.key8 != '1':
        return "Finish the last round you sneaky KID!"
    else:
        nextKey = temp_data.key9
        form = GetAnswer()
        user = User.query.filter_by(id = g.user.id).first()
        if form.validate_on_submit():
            if form.answer.data == temp_data.ans_round9:
                user.key9 = '1'                   
                db.session.add(user)
                db.session.commit()
        elif request.method == 'POST':
            print('Incoming..')
            print(request.get_json())  # parse as JSON 
            tempdata = request.get_json()
            HINT = [g.user.hint1, g.user.hint2, g.user.hint3, g.user.hint4, g.user.hint5, g.user.hint6, g.user.hint7]
            if HINT[0] == None:
                user.hint1 = tempdata['hint'] 
                #user.time1 = tempdata['time']
            elif HINT[1] == None:
                user.hint2 = tempdata['hint']
                #user.time2 = tempdata['time']
            elif HINT[2] == None:
                user.hint3 = tempdata['hint']
                #user.time3 = tempdata['time']
            elif HINT[3] == None:
                user.hint4 = tempdata['hint']
                #user.time4 = tempdata['time']
            elif HINT[4] == None:
                user.hint5 = tempdata['hint']
                #user.time5 = tempdata['time']
            elif HINT[5] == None:
                user.hint6 = tempdata['hint']
                #user.time6 = tempdata['time']
            elif HINT[6] == None:
                user.hint7 = tempdata['hint']
                #user.time7 = tempdata['time']

                
            user.time1 = tempdata['time']
            user.hints =   int(g.user.hints) - 1                 
            db.session.add(user)
            db.session.commit()
            return 'OK', 200
        return render_template("round8.html", form=form ,nextKey=nextKey,hinttimer=hinttimer)







@app.route('/logout')
@login_required
def logout():
    
    logout_user()
    return redirect(url_for('welcome'))




if __name__ == '__mainn__' :
    app.run()










    