from flask import Flask, request

app = Flask(__name__)

@app.route('/filter')
def filter_items():
    type_ = request.args.get('type')
    color = request.args.get('color')
    size = request.args.get('size')
    return f"Type: {type_}, Color: {color}, Size: {size}"

if __name__ == '__main__':
    app.run(debug=True)
