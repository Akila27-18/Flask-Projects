from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Sample travel deals
deals = [
    {'destination': 'paris', 'price': '$800'},
    {'destination': 'tokyo', 'price': '$1200'},
    {'destination': 'paris', 'price': '$750'},
    {'destination': 'london', 'price': '$950'}
]

# Route 1: Booking Form
@app.route('/booking', methods=['GET'])
def booking_form():
    return render_template_string("""
        <h2>Travel Booking Enquiry</h2>
        <form method="post" action="{{ url_for('handle_booking') }}">
            Name: <input type="text" name="name" required><br><br>
            Destination: <input type="text" name="destination" required><br><br>
            Travel Date: <input type="date" name="date" required><br><br>
            <button type="submit">Submit Booking</button>
        </form>
    """)

# Route 2: Handle POST and Redirect
@app.route('/booking', methods=['POST'])
def handle_booking():
    name = request.form['name']
    # You can optionally store destination and date here
    return redirect(url_for('confirm_booking', name=name))

# Route 3: Confirmation Page with Dynamic URL
@app.route('/booking/confirm/<name>')
def confirm_booking(name):
    return f"<h2>Booking confirmed! Thank you, {name}.</h2>"

# Route 4: Deals Filtering via Query Param
@app.route('/deals')
def travel_deals():
    dest = request.args.get('destination')
    filtered = [deal for deal in deals if deal['destination'].lower() == dest.lower()] if dest else deals

    html = "<h2>Available Deals:</h2><ul>"
    for deal in filtered:
        html += f"<li>{deal['destination'].title()} - {deal['price']}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
