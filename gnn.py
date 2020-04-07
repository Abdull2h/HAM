from flask import Flask,render_template,request,session,redirect,url_for
from flask_mail import Mail, Message
from data import storeData,readData
from datetime import timedelta
from json import dumps
from waitress import serve
import os


app = Flask(__name__)
app.secret_key='c757593904c759f0b8b463ee0165bced'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'moh.daim996@gmail.com'
app.config['MAIL_PASSWORD'] = 'pmnntklzpsedbrim'

mail = Mail(app)

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home():
    
    return render_template('index.html', title = 'Home Page')
@app.route("/about_us.html")
@app.route("/about_us")
def about_us():
    return render_template('about_us.html', title = 'About Us')

@app.route("/contact_us.html")
@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html', title = 'Contact Us')
@app.route("/send", methods=['POST','GET'])
def sendM():
    email = request.form['email']
    name = request.form['name']
    body = request.form['body']
    phone = request.form['phone']
    msg = Message(f'{name} {email}',sender='moh.daim996@gmail.com', recipients=['moh.daim996@gmail.com'])
    msg.body=f'''a message from: { name }
     message:
     { body }
    {email}
    {phone}
    '''
    mail.send(msg)
    return render_template('/index.html',
            message=f"{name}, your message has been sent. we'll contact you on: {email} or {phone}",
            msgStat=True,
            title = 'Home Page')
   
@app.route("/regestration.html")
@app.route("/regestration")
def register():
    if session.get('logged_in') == True:
        return redirect('/index.html')
    return render_template('regestration.html', title = 'Register')

@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    us = request.form['name']
    pw = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    members = readData('data.json')
    if us in members:
        return render_template('regestration.html', 
        us = us,
        pw = pw,
        email = email,
        phone = phone,
        errmsg=True,
        title = 'Register')
    else:
        storeData(members, 'data.json', 'data','none', us, pw, phone, email)
        return render_template(
            'index.html',
            message=f"{us} is registered, {email},{phone}",
            msgStat=True,
            title = 'Home Page')


@app.route("/login.html")
@app.route("/login")
def login():
    if session.get('logged_in') == True:
        return redirect('/index.html')
    return render_template('login.html', title = 'Login')
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/users.html")
@app.route("/users")
def users():
    return render_template('users.html', title = 'Users List')

@app.route('/set', methods=['POST', 'GET'])
def set():
    us = request.form['name']
    pw = request.form['password']
    data = readData('data.json')
    for name in data.keys():
        if us == name:
            if pw == data[name]['pass']:
                session['current_user'] = us
                session['logged_in']=True
                return redirect('/index.html')
            else:
                return render_template('login.html', message=f"Wrong password",
            errmsg=True, title = 'Login')
        
    return render_template('login.html', message=f"Wrong username",
            errmsg=True,title = 'Login')

@app.route('/get/')
def get():
    if session.get('logged_in') == True:
        return 'You are logged in'
    return 'You are not logged in'

@app.route('/pop/')
def pop():
    session.pop('current_user')
    session.pop('logged_in')
    return redirect('/index.html')

@app.route('/<string:cat>')
def cat(cat):
    getgame = readData('games.json')
    try:
        game=getgame[cat]
        return render_template('cat_page.html', title=cat.capitalize(), game=game)
    except KeyError:
        return render_template('404.html',title='Error - 404'), 404

@app.errorhandler(404)
def err_404(error):
   return render_template('404.html',title='Error - 404'), 404


if __name__ == '__main__':
   # print("-- DEBUG MODE ----")
   # app.run(debug=True, port='5091')

   print("--- PRODUCTION MODE ---")
   p = os.environ.get('PORT')
   p = '5000' if p == None else p
   serve(app, host='0.0.0.0', port=p)
