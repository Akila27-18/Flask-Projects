from flask import Flask, request, redirect, url_for, render_template_string
from datetime import datetime

app = Flask(__name__)

# In-memory subscriber list
subscribers = []

# Subscription form HTML
form_html = '''
<!DOCTYPE html>
<html>
<head><title>Newsletter Subscription</title></head>
<body>
  <h2>Subscribe to Our Newsletter</h2>
  <form method="POST">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    <button type="submit">Subscribe</button>
  </form>
</body>
</html>
'''

# GET form and POST handler on same route
@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        month = datetime.now().strftime("%B")  # e.g., July
        subscribers.append({'name': name, 'email': email, 'month': month})
        return redirect(url_for('thanks', name=name))
    return form_html

# Confirmation route
@app.route('/thanks/<name>')
def thanks(name):
    return f"<h2>Thank you, {name}, for subscribing to our newsletter!</h2>"

# Show filtered subscriber list by month
@app.route('/subscribers')
def list_subscribers():
    month = request.args.get('month')
    filtered = [s for s in subscribers if s['month'].lower() == month.lower()] if month else subscribers

    output = f"<h2>Subscribers in {month or 'All Months'}</h2><ul>"
    for sub in filtered:
        output += f"<li>{sub['name']} – {sub['email']} ({sub['month']})</li>"
    output += "</ul>"
    return output

if __name__ == '__main__':
    app.run(debug=True)
