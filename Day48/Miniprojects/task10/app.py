from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products')
def show_products():
    products = [
        {'name': 'Smartphone', 'price': 499.99, 'in_stock': True, 'image': 'phone.png'},
        {'name': 'Laptop', 'price': 899.99, 'in_stock': False, 'image': 'laptop.png'},
        {'name': 'Tablet', 'price': 299.99, 'in_stock': True, 'image': 'phone.png'}
    ]
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
