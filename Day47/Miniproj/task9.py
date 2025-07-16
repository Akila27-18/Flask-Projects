from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Dummy product serial and warranty data
warranty_data = {
    'ABC123': '2 years',
    'XYZ789': '1 year',
    'DEF456': '3 years',
}

product_warranty = {
    'laptop': '2 years',
    'phone': '1 year',
    'printer': '3 years'
}

@app.route('/check-warranty', methods=['GET', 'POST'])
def check_warranty():
    return '''
    <h2>Product Warranty Checker</h2>
    <form method="POST" action="/result">
        Enter Product Serial: <input type="text" name="serial" required><br><br>
        <input type="submit" value="Check Warranty">
    </form>
    '''

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        serial = request.form.get('serial')
        return redirect(url_for('result', serial=serial))

    # GET request handling
    serial = request.args.get('serial')
    warranty = warranty_data.get(serial.upper(), 'No warranty information found.')

    return f'''
    <h2>Warranty Result</h2>
    <p>Serial: <strong>{serial}</strong></p>
    <p>Warranty: <strong>{warranty}</strong></p>
    <a href="/confirmation">Continue</a>
    '''

@app.route('/warranty/<product>')
def warranty(product):
    warranty = product_warranty.get(product.lower())
    if warranty:
        return f"<h2>{product.title()} Warranty</h2><p>{warranty}</p>"
    else:
        return f"<h2>{product.title()}</h2><p>No warranty info available.</p>"

@app.route('/confirmation')
def confirmation():
    return "<h2>Warranty Check Complete</h2><p>Thank you for using our service.</p>"

if __name__ == '__main__':
    app.run(debug=True)
