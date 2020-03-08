from flask import Flask,render_template,request


app = Flask(__name__)
@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html', title = 'Home Page')
    
@app.route("/about_us.html")
def about_us():
    return render_template('about_us.html', title = 'About Us')

@app.route("/contact_us.html")
def contact_us():
    return render_template('contact_us.html', title = 'Contact Us')

@app.route("/regestration.html")
def register():
    return render_template('regestration.html', title = 'Register')

@app.route("/login.html")
def login():
    return render_template('login.html', title = 'Login')

@app.route("/users.html")
def users():
    return render_template('users.html', title = 'Users List')

@app.route("/action.html")
def action():
    return render_template('action.html', title = 'Action Games')

@app.route("/sport.html")
def sport():
    return render_template('sport.html', title = 'Sport Games')

@app.route("/adventure.html")
def adventure():
    return render_template('adventure.html', title = 'Adventure Games')

if __name__ == '__main__':
    app.run(debug=True)
