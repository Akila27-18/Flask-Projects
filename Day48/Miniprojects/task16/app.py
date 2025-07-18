from flask import Flask, render_template

app = Flask(__name__)

faqs = [
    {"question": "What is Flask?", "answer": "Flask is a lightweight WSGI web framework in Python."},
    {"question": "How do I install Flask?", "answer": "Use pip install flask in your terminal."},
    {"question": "Is this project open source?", "answer": ""},
    {"question": "How to deploy a Flask app?", "answer": "You can deploy with platforms like Render, Replit, or Heroku."}
]

@app.route("/faq")
def faq():
    return render_template("faq.html", faqs=faqs)

if __name__ == "__main__":
    app.run(debug=True)
