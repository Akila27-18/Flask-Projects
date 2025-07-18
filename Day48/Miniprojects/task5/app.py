from flask import Flask, render_template

app = Flask(__name__)

@app.route('/jobs')
def job_list():
    jobs = [
        {'title': 'Frontend Developer', 'company': 'TechNova', 'remote': True, 'logo': 'company1.png'},
        {'title': 'Backend Engineer', 'company': 'CodeNest', 'remote': False, 'logo': 'company2.png'},
        {'title': 'Data Analyst', 'company': 'InsightIQ', 'remote': True, 'logo': 'company1.png'}
    ]
    return render_template('jobs.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
