from flask import Flask

app = Flask(__name__)



# 2. Square of a number
@app.route('/square/<int:number>')
def square(number):
    return f"The square of {number} is {number ** 2}"



if __name__ == '__main__':
    app.run(debug=True)
