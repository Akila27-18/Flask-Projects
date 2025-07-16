from flask import Flask, request

app = Flask(__name__)

@app.route('/safe', methods=['POST'])
def safe():
    name = request.form.get('name', 'Anonymous')
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)
