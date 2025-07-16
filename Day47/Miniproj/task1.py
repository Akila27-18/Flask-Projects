from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory storage for feedbacks
feedback_list = []

# Route 1: Feedback Form
@app.route('/feedback-form', methods=['GET'])
def feedback_form():
    return render_template_string("""
        <h2>Customer Feedback Form</h2>
        <form action="{{ url_for('submit_feedback') }}" method="post">
            Name: <input type="text" name="name" required><br><br>
            Email: <input type="email" name="email" required><br><br>
            Message: <textarea name="message" required></textarea><br><br>
            <button type="submit">Submit</button>
        </form>
    """)

# Route 2: Handle POST and Redirect
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    feedback_list.append({'name': name, 'email': email, 'message': message})
    return redirect(url_for('thank_you'))

# Route 3: Thank You Page
@app.route('/thank-you')
def thank_you():
    return "<h2>Thank you for your feedback!</h2>"

# Route 4: Filtered Feedback via Query Param
@app.route('/feedbacks')
def feedbacks():
    user_filter = request.args.get('user')
    filtered = [f for f in feedback_list if f['name'] == user_filter] if user_filter else feedback_list

    html = "<h2>Feedbacks:</h2><ul>"
    for fb in filtered:
        html += f"<li><b>{fb['name']}</b> ({fb['email']}): {fb['message']}</li>"
    html += "</ul>"
    return html

# Route 5: Dynamic User-Specific Page
@app.route('/user/<username>')
def user_profile(username):
    user_feedbacks = [f for f in feedback_list if f['name'].lower() == username.lower()]
    if not user_feedbacks:
        return f"<h2>No feedback found for user: {username}</h2>"

    html = f"<h2>Feedback from {username}:</h2><ul>"
    for fb in user_feedbacks:
        html += f"<li>{fb['message']} (Email: {fb['email']})</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
