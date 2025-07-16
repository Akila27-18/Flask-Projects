from flask import Flask, request

app = Flask(__name__)

@app.route('/debug')
def debug():
    if request.args.get('debug') == 'true':
        return "Debug mode is ON"
    return "Debug mode is OFF"

if __name__ == '__main__':
    app.run(debug=True)
