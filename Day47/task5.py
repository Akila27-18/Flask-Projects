from flask import Flask

app = Flask(__name__)



# 5. Price display with decimal
@app.route('/price/<float:amount>')
def show_price(amount):
    return f"The price is ₹{amount:.2f}"



if __name__ == '__main__':
    app.run(debug=True)
