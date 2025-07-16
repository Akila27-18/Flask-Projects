from flask import Flask

app = Flask(__name__)


# 6. Mini HTML Profile
@app.route('/profile/<username>')
def profile(username):
    return f"""
    <h2>User Profile</h2>
    <p>Name: <strong>{username}</strong></p>
    """



if __name__ == '__main__':
    app.run(debug=True)
