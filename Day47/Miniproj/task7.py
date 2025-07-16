from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Dummy course data
courses = [
    {'code': 'CS101', 'name': 'Intro to Computer Science', 'dept': 'CS'},
    {'code': 'CS102', 'name': 'Data Structures', 'dept': 'CS'},
    {'code': 'MATH201', 'name': 'Calculus I', 'dept': 'Math'},
    {'code': 'PHY101', 'name': 'Physics Basics', 'dept': 'Physics'}
]

@app.route('/courses')
def course_list():
    dept = request.args.get('dept')
    if dept:
        filtered = [c for c in courses if c['dept'].lower() == dept.lower()]
    else:
        filtered = courses

    html = "<h2>Course List</h2><ul>"
    for c in filtered:
        html += f"<li>{c['code']}: {c['name']} ({c['dept']})</li>"
    html += "</ul>"

    html += '''
    <p>Filter: <a href="/courses?dept=CS">CS</a> |
    <a href="/courses?dept=Math">Math</a> |
    <a href="/courses?dept=Physics">Physics</a></p>
    '''

    return html


@app.route('/register')
def register():
    form_html = '''
    <h2>Course Registration</h2>
    <form action="/register" method="POST">
      Student Name: <input type="text" name="student" required><br><br>
      Course Code: <input type="text" name="course" required><br><br>
      <button type="submit">Register</button>
    </form>
    '''
    return form_html


@app.route('/register', methods=['POST'])
def process_registration():
    student = request.form['student']
    # course = request.form['course']  # You can store or process this as needed
    return redirect(url_for('confirm_registration', name=student))


@app.route('/confirm-registration/<name>')
def confirm_registration(name):
    return f"<h2>Thank you, {name}! 🎓</h2><p>Your course registration is confirmed.</p>"

if __name__ == '__main__':
    app.run(debug=True)
