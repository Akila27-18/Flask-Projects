from flask import Flask, render_template

app = Flask(__name__)

# Dummy data
name = "Akila"
skills = ["Python", "Flask", "HTML", "CSS", "JavaScript"]
projects = [
    {"title": "Portfolio Website", "description": "A personal portfolio using Flask."},
    {"title": "Weather App", "description": "Displays current weather of any city."},
    {"title": "Task Manager", "description": "A to-do app with SQLite backend."}
]
available_for_hire = True

@app.route("/")
def home():
    return render_template("home.html", name=name, available=available_for_hire)

@app.route("/about")
def about():
    return render_template("about.html", name=name, skills=skills)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
