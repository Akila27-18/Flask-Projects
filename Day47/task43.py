from flask import Flask, request

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def log_form():
    print("Form Data Received:", dict(request.form))
    return "Form data printed to terminal."

if __name__ == "__main__":
    app.run(debug=True)
