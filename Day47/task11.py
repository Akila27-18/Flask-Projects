from flask import Flask

app = Flask(__name__)



# 11. Username check
@app.route('/user/<username>')
def user_check(username):
    allowed_users = ['akila', 'rahul', 'meena']
    if username.lower() in allowed_users:
        return f"Welcome back, {username}!"
    else:
        return "User not found."


if __name__ == '__main__':
    app.run(debug=True)
