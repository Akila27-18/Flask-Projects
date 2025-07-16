from flask import Flask, request

app = Flask(__name__)

@app.route('/method-check', methods=['GET', 'POST'])
def method_check():
    return f"Current method: {request.method}"

if __name__ == "__main__":
    app.run(debug=True)
