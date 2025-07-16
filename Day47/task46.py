from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to the Home Page!"

@app.route('/start')
def start():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
