from flask import Flask, request

app = Flask(__name__)

@app.route('/table')
def show_table():
    html = "<table border='1'><tr><th>Key</th><th>Value</th></tr>"
    for key, value in request.args.items():
        html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    html += "</table>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
