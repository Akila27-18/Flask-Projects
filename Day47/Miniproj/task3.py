from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Store RSVP data in-memory
guests = []

# HTML form template for RSVP
rsvp_form = '''
<!DOCTYPE html>
<html>
<head><title>RSVP</title></head>
<body>
  <h2>Event RSVP Form</h2>
  <form method="POST" action="/rsvp-confirm">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Attending: 
    <select name="attending">
      <option value="yes">Yes</option>
      <option value="no">No</option>
    </select><br><br>
    <button type="submit">Submit RSVP</button>
  </form>
</body>
</html>
'''

# Route to show RSVP form
@app.route('/rsvp')
def rsvp():
    return rsvp_form

# Handle form submission
@app.route('/rsvp-confirm', methods=['POST'])
def rsvp_confirm():
    name = request.form['name']
    email = request.form['email']
    attending = request.form['attending']
    guests.append({'name': name, 'email': email, 'attending': attending})
    return redirect(url_for('thank_you', name=name))

# Personalized thank-you route
@app.route('/thank-you/<name>')
def thank_you(name):
    return f"<h2>Thank you, {name}, for your RSVP!</h2>"

# Guests listing filtered by query parameter
@app.route('/guests')
def guest_list():
    attending_filter = request.args.get('attending')
    if attending_filter:
        filtered = [g for g in guests if g['attending'] == attending_filter.lower()]
    else:
        filtered = guests

    output = "<h2>Guest List</h2><ul>"
    for guest in filtered:
        output += f"<li>{guest['name']} – Attending: {guest['attending']}</li>"
    output += "</ul>"
    return output

if __name__ == '__main__':
    app.run(debug=True)
