from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        return f"Registered: {name} ({email})"
    return '''
    <form method="post">
        Name: <input name="name"><br>
        Email: <input name="email"><br>
        Password: <input name="password" type="password"><br>
        <button type="submit">Register</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
