from flask import Flask, request

app = Flask(__name__)

@app.route('/both-methods', methods=['GET', 'POST'])
def both_methods():
    return f"Request used method: {request.method}"

if __name__ == "__main__":
    app.run(debug=True)
