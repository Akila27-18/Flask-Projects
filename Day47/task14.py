from flask import Flask

app = Flask(__name__)


# 14. HTML with triple quotes
@app.route('/welcome/<name>')
def welcome(name):
    return f"""
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Welcome, {name}!</h1>
        <p>This is a custom HTML page using Flask and triple quotes.</p>
    </body>
    </html>
    """



if __name__ == '__main__':
    app.run(debug=True)
