from flask import Flask,render_template,request,session,redirect
from data import storeData,readData


app = Flask(__name__)
app.secret_key='c757593904c759f0b8b463ee0165bced'

   
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
    umail = request.form['email']
    phone = request.form['phone']
    members = readData('data.json')
    if us in members:
        return render_template('regestration.html', 
        us = us,
        pw = pw,
        umail = umail,
        phone = phone,
        errmsg=True)
    else:
        storeData(members, 'data.json', 'data','none', us, pw, phone, umail)
        return render_template(
            'index.html',
            message=f"{us} is registered, {umail},{phone}",
            msgStat=True)


@app.route("/login.html")
@app.route("/login")
def login():
    if session.get('logged_in') == True:
        return redirect('/index.html')
    return render_template('login.html', title = 'Login')

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
    return f"cuurent_user is removed"
app.run(debug=True)
