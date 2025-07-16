from flask import Flask, request

app = Flask(__name__)

@app.route('/display/<name>')
def display(name):
    age = request.args.get('age', 'unknown')
    return f"Name: {name}, Age: {age}"

if __name__ == '__main__':
    app.run(debug=True)
