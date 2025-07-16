from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory list to store complaints
complaints = []

# Route 1: Complaint Form
@app.route('/complaint', methods=['GET'])
def complaint_form():
    return render_template_string("""
        <h2>Customer Complaint Form</h2>
        <form method="post" action="{{ url_for('complaint_submit') }}">
            Name: <input type="text" name="name" required><br><br>
            Issue: <textarea name="issue" required></textarea><br><br>
            Urgency:
            <select name="urgency" required>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
            </select><br><br>
            <button type="submit">Submit Complaint</button>
        </form>
    """)

# Route 2: Handle Submission and Redirect
@app.route('/complaint-submit', methods=['POST'])
def complaint_submit():
    name = request.form['name']
    issue = request.form['issue']
    urgency = request.form['urgency']
    complaints.append({'name': name, 'issue': issue, 'urgency': urgency})
    return redirect(url_for('complaint_status', name=name))

# Route 3: Status Page (Dynamic)
@app.route('/complaint-status/<name>')
def complaint_status(name):
    user_complaints = [c for c in complaints if c['name'].lower() == name.lower()]
    if not user_complaints:
        return f"<h3>No complaint found for {name}.</h3>"

    html = f"<h2>Complaints for {name}</h2><ul>"
    for c in user_complaints:
        html += f"<li><b>Issue:</b> {c['issue']} <br> <b>Urgency:</b> {c['urgency'].title()}</li><br>"
    html += "</ul>"
    return html

# Route 4: Filter Complaints by Urgency
@app.route('/complaints')
def complaint_filter():
    urgency_filter = request.args.get('urgency')
    if urgency_filter:
        filtered = [c for c in complaints if c['urgency'].lower() == urgency_filter.lower()]
    else:
        filtered = complaints

    html = "<h2>Complaints List</h2><ul>"
    for c in filtered:
        html += f"<li><b>{c['name']}</b>: {c['issue']} (Urgency: {c['urgency']})</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
