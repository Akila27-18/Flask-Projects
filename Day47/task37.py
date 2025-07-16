from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Submitted by: {name}"

if __name__ == "__main__":
    app.run(debug=True)
