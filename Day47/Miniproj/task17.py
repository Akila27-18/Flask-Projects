from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Store certificates in memory
certificates = []

@app.route('/quiz-form')
def quiz_form():
    return '''
    <h2>Quiz Certificate Form</h2>
    <form action="/submit-quiz" method="POST">
        Name: <input type="text" name="name" required><br><br>
        Score: <input type="number" name="score" required min="0" max="10"><br><br>
        <button type="submit">Generate Certificate</button>
    </form>
    '''

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    name = request.form['name']
    score = request.form['score']
    # Save certificate
    certificates.append({'name': name, 'score': int(score)})
    return redirect(url_for('show_certificate', name=name, score=score))


@app.route('/certificate/<name>/<int:score>')
def show_certificate(name, score):
    return f'''
    <h2>🎓 Certificate of Completion</h2>
    <p>This is to certify that <strong>{name}</strong> scored <strong>{score}/10</strong> on the quiz.</p>
    '''

@app.route('/certificates')
def certificate_list():
    filter_score = request.args.get('score')
    if filter_score:
        try:
            score_val = int(filter_score)
            filtered = [c for c in certificates if c['score'] == score_val]
        except ValueError:
            return '<p>Invalid score filter.</p>'
    else:
        filtered = certificates

    if not filtered:
        return '<h3>No certificates found.</h3>'

    html = '<h2>Certificates</h2><ul>'
    for c in filtered:
        link = url_for('show_certificate', name=c['name'], score=c['score'])
        html += f"<li>{c['name']} – Score: {c['score']} – <a href='{link}'>View Certificate</a></li>"
    html += '</ul>'
    return html

if __name__ == '__main__':
    app.run(debug=True)

