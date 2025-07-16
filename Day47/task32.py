from flask import Flask, request

app = Flask(__name__)

@app.route('/count-params')
def count_params():
    return f"Total query parameters: {len(request.args)}"

if __name__ == '__main__':
    app.run(debug=True)
