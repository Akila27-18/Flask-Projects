from flask import Flask, request

app = Flask(__name__)

@app.route('/profile')
def profile():
    mode = request.args.get('mode', 'user')
    return f"Profile mode: {mode}"

if __name__ == '__main__':
    app.run(debug=True)
