from flask import Flask,render_template,request,session,redirect,url_for
from flask_mail import Mail, Message
from data import storeData,readData
from datetime import timedelta


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
            msgStat=True)
   
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
        errmsg=True)
    else:
        storeData(members, 'data.json', 'data','none', us, pw, phone, email)
        return render_template(
            'index.html',
            message=f"{us} is registered, {email},{phone}",
            msgStat=True)


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

@app.route("/action.html")
@app.route("/action")
def action():
    getpost = readData('posts.json')
    post=getpost['action']
    return render_template('action.html', title = 'Action Games',post=post)

@app.route("/sport.html")
@app.route("/sport")
def sport():
    getpost = readData('posts.json')
    post=getpost['sports']
    return render_template('sport.html', title = 'Sport Games', post = post)

@app.route("/adventure.html")
@app.route("/adventure")
def adventure():
    getpost = readData('posts.json')
    post=getpost['adventure']
    return render_template('adventure.html', title = 'Adventure Games',post=post)

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
                return render_template('login.html', us = 'wrong pass')
        
    return render_template('login.html', us='wrong username')

    

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
@app.errorhandler(404)
def err_404(error):
   return render_template('404.html',title='Error - 404'), 404

app.run(debug=True)
