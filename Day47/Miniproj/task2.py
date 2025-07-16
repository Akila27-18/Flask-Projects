from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Temporary in-memory storage for applicants
applicants = []

# HTML Form Template for /apply
apply_form = '''
<!DOCTYPE html>
<html>
<head><title>Job Application</title></head>
<body>
  <h2>Job Application Form</h2>
  <form action="/submit-application" method="POST">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Position: <input type="text" name="position" required><br><br>
    <button type="submit">Apply</button>
  </form>
</body>
</html>
'''

@app.route('/apply')
def apply():
    return apply_form


@app.route('/submit-application', methods=['POST'])
def submit_application():
    name = request.form['name']
    email = request.form['email']
    position = request.form['position']
    # Save to in-memory list
    applicants.append({'name': name, 'email': email, 'position': position})
    return redirect(url_for('application_status'))


@app.route('/application-status')
def application_status():
    return '''
    <h2>Application Submitted Successfully!</h2>
    <p>Thank you for applying. We will contact you soon.</p>
    '''


@app.route('/applications')
def view_applications():
    position_filter = request.args.get('position')
    if position_filter:
        filtered = [a for a in applicants if a['position'].lower() == position_filter.lower()]
    else:
        filtered = applicants

    if not filtered:
        return '<h3>No applications found for that position.</h3>'

    html = '<h2>Applications</h2><ul>'
    for a in filtered:
        html += f"<li>{a['name']} – {a['position']} – <a href='/applicant/{a['name']}'>View</a></li>"
    html += '</ul>'
    return html


@app.route('/applicant/<name>')
def view_applicant(name):
    for a in applicants:
        if a['name'].lower() == name.lower():
            return f'''
            <h2>Applicant Profile: {a["name"]}</h2>
            <p><strong>Email:</strong> {a["email"]}</p>
            <p><strong>Position:</strong> {a["position"]}</p>
            '''
    return '<h3>Applicant not found.</h3>'


if __name__ == '__main__':
    app.run(debug=True)
