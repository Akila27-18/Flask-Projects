
from flask import Flask

app = Flask(__name__)



# 7. Math operations
@app.route('/math/<int:x>/<int:y>')
def math_ops(x, y):
    return f"Sum: {x+y}, Difference: {x-y}, Product: {x*y}"

#
if __name__ == '__main__':
    app.run(debug=True)
