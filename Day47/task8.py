from flask import Flask

app = Flask(__name__)



# 8. Path converter
@app.route('/file/<path:filename>')
def file_path(filename):
    return f"You requested the file: {filename}"


if __name__ == '__main__':
    app.run(debug=True)
