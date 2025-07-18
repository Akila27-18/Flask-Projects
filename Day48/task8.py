from flask import Flask, render_template

app = Flask(__name__)


@app.route('templates/index.html')
def index():
    username = "Alex"
    return render_template('index.html', title="Home", username=username)

if __name__ == '__main__':
    app.run(debug=True)