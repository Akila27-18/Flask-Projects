from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html", username="Mahesh")

@app.route('/skills')
def skills():
    tech = ["Python", "Flask", "Jinja"]
    return render_template("skills.html", skills=tech)

@app.route('/status')
def status():
    return render_template("status.html", logged_in=True)

@app.route('/scores')
def scores():
    return render_template("scores.html", scores=[75, 89, 62, 95])

@app.route('/empty')
def empty():
    return render_template("empty.html", items=[])

@app.route('/date')
def date():
    return render_template("date.html", now=datetime.now())

@app.route('/profile')
def profile():
    user = {"name": "Mahesh", "age": 30, "role": "admin"}
    return render_template("profile.html", user=user)

@app.route('/welcome/<name>')
def welcome(name):
    return render_template("welcome.html", name=name)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", role="admin")

@app.route('/products')
def products():
    products = [
        {"name": "Laptop", "price": "$999"},
        {"name": "Phone", "price": "$699"}
    ]
    return render_template("products.html", products=products)

@app.route('/htmltext')
def htmltext():
    text = "<strong>Bold text</strong> with <em>HTML</em>"
    return render_template("htmltext.html", text=text)

if __name__ == '__main__':
    app.run(debug=True)
