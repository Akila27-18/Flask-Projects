from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def result():
    student_name = "Akila Sharma"
    subjects = {
        "Math": 92,
        "Science": 85,
        "English": 78,
        "History": 88,
        "Computer": 95
    }

    average = sum(subjects.values()) / len(subjects)

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    else:
        grade = 'C'

    return render_template('result.html', name=student_name, subjects=subjects, grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
