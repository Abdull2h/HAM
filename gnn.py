from flask import Flask,render_template,request


app = Flask(__name__)
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
    return render_template('action.html', title = 'Action Games')

@app.route("/sport.html")
@app.route("/sport")
def sport():
    return render_template('sport.html', title = 'Sport Games')

@app.route("/adventure.html")
@app.route("/adventure")
def adventure():
    return render_template('adventure.html', title = 'Adventure Games')

if __name__ == '__main__':
    app.run(debug=True)
