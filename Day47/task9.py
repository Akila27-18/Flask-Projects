from flask import Flask

app = Flask(__name__)


# 9. Color text
@app.route('/color/<string:color>')
def color_text(color):
    return f"<p style='color:{color}'>This is {color} text</p>"



if __name__ == '__main__':
    app.run(debug=True)
