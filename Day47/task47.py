from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    logged_in = False  # simulate login state
    if not logged_in:
        return redirect(url_for('login'))
    return "Welcome to the Dashboard!"

@app.route('/login')
def login():
    return "Please login to continue."

if __name__ == "__main__":
    app.run(debug=True)
