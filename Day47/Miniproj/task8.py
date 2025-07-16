from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory bug store
bug_reports = []
bug_id_counter = 1

# HTML form for bug report
report_form = '''
<!DOCTYPE html>
<html>
<head><title>Bug Report</title></head>
<body>
  <h2>Report a Bug</h2>
  <form method="POST" action="/submit-report">
    Title: <input type="text" name="title" required><br><br>
    Description: <textarea name="description" required></textarea><br><br>
    Priority:
    <select name="priority">
      <option value="low">Low</option>
      <option value="medium">Medium</option>
      <option value="high">High</option>
    </select><br><br>
    <button type="submit">Submit Report</button>
  </form>
</body>
</html>
'''

# Route to show report form
@app.route('/report')
def report():
    return report_form

# Handle bug submission
@app.route('/submit-report', methods=['POST'])
def submit_report():
    global bug_id_counter
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    
    bug_reports.append({
        'id': bug_id_counter,
        'title': title,
        'description': description,
        'priority': priority
    })
    bug_id_counter += 1
    return redirect(url_for('report_confirm'))

# Confirmation page
@app.route('/report-confirm')
def report_confirm():
    return "<h2>Your bug report has been submitted successfully!</h2>"

# List bugs filtered by priority
@app.route('/bugs')
def list_bugs():
    priority_filter = request.args.get('priority')
    if priority_filter:
        filtered = [b for b in bug_reports if b['priority'] == priority_filter.lower()]
    else:
        filtered = bug_reports

    output = "<h2>Bug Reports</h2><ul>"
    for bug in filtered:
        output += f"<li><a href='/bug/{bug['id']}'>{bug['title']}</a> – Priority: {bug['priority']}</li>"
    output += "</ul>"
    return output

# Dynamic bug detail route
@app.route('/bug/<int:id>')
def bug_detail(id):
    bug = next((b for b in bug_reports if b['id'] == id), None)
    if bug:
        return f"""
        <h2>Bug ID: {bug['id']}</h2>
        <p><strong>Title:</strong> {bug['title']}</p>
        <p><strong>Description:</strong> {bug['description']}</p>
        <p><strong>Priority:</strong> {bug['priority'].capitalize()}</p>
        """
    else:
        return "<h2>Bug not found.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
