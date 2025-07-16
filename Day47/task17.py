from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    return "Form submitted successfully using POST."

if __name__ == "__main__":
    app.run(debug=True)
