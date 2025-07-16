from flask import Flask

app = Flask(__name__)



# 3. Greet with name and age
@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return f"Hi {name}, you are {age} years old."


if __name__ == '__main__':
    app.run(debug=True)
