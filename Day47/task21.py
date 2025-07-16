from flask import Flask, request

app = Flask(__name__)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return "POST not allowed here!", 405
    return "Welcome to the admin page."

if __name__ == "__main__":
    app.run(debug=True)
