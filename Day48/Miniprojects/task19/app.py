from flask import Flask, render_template

app = Flask(__name__)

# Sample route for testing 500 error
@app.route('/cause-error')
def cause_error():
    return 1 / 0  # Intentional error

# Home route
@app.route('/')
def home():
    return '<h1>Welcome to the Homepage</h1>'

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=str(e)), 404

# Custom 500 error handler
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html', error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
