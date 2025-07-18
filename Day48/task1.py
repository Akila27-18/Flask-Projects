from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs("templates", exist_ok=True)
    with open("templates/index.html", "w") as f:
        f.write("<h1>Welcome to Flask</h1>")
    app.run(debug=True)
