from flask import Flask, render_template

app = Flask(__name__)

@app.route("/courses")
def courses():
    course_list = [
        {"title": "Web Development", "instructor": "John Doe", "duration": "6 weeks", "level": "beginner"},
        {"title": "Data Science", "instructor": "Jane Smith", "duration": "8 weeks", "level": "advanced"},
        {"title": "Machine Learning", "instructor": "Emily Chen", "duration": "10 weeks", "level": "intermediate"},
        {"title": "Cybersecurity", "instructor": "Alan Turing", "duration": "5 weeks", "level": "advanced"},
    ]
    return render_template("courses.html", courses=course_list)

if __name__ == "__main__":
    app.run(debug=True)
