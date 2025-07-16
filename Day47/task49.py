from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    home = url_for('home')
    about = url_for('about')
    return f'''
    <h2>Navigation</h2>
    <ul>
        <li><a href="{home}">Home</a></li>
        <li><a href="{about}">About</a></li>
    </ul>
    '''

@app.route('/home')
def home():
    return "This is Home Page"

@app.route('/about')
def about():
    return "This is About Page"

if __name__ == "__main__":
    app.run(debug=True)
