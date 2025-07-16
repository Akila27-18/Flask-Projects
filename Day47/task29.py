from flask import Flask, request

app = Flask(__name__)

@app.route('/params')
def show_params():
    html = "<ul>"
    for key, value in request.args.items():
        html += f"<li>{key}: {value}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
