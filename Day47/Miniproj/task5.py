from flask import Flask, request, render_template, redirect, url_for, flash
from flask import session
from flask import get_flashed_messages

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

departments = ['Sales', 'Support', 'HR', 'Technical']

@app.route('/contact', methods=['GET'])
def contact():
    messages = get_flashed_messages()
    return render_template('contact.html', departments=departments, messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    department = request.form.get('department')
    source = request.args.get('source', 'direct')

    print(f"[SOURCE: {source}] Contact from {name} ({email}) to {department}: {message}")

    flash('Thank you for contacting us! We will respond shortly.')
    return redirect(url_for('thank_you'))

@app.route('/contact/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/contact/<department>')
def department_info(department):
    if department.capitalize() not in departments:
        return f"<h2>No such department: {department}</h2>", 404
    return f"<h2>Welcome to the {department.capitalize()} Department Contact Page</h2><p>Please reach out via the contact form.</p>"
