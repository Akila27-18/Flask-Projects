from flask import Flask, url_for

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return f"User Profile: {username}"

@app.route('/')
def index():
    profile_link = url_for('profile', username='mahesh')
    return f'<a href="{profile_link}">Go to Mahesh\'s Profile</a>'

if __name__ == "__main__":
    app.run(debug=True)
