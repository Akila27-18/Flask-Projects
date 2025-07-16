from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <form action="/login" method="post">
        <input name="username" placeholder="Enter Username">
        <button type="submit">Login</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
