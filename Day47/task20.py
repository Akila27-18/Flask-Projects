from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"Welcome, {username}!"
    return '''
    <form method="post">
        <input name="username" placeholder="Enter Username">
        <button type="submit">Login</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
