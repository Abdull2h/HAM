from flask import Flask,render_template,request
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

app.run(debug=True)
