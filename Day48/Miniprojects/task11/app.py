from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

news_list = [
    {
        "title": "Global Markets Rally as Inflation Cools",
        "category": "business",
        "timestamp": datetime(2025, 7, 17, 9, 30),
        "is_breaking": False
    },
    {
        "title": "Earthquake Shakes Northern Region",
        "category": "world",
        "timestamp": datetime(2025, 7, 17, 11, 0),
        "is_breaking": True
    },
    {
        "title": "New AI Tool Revolutionizes Education",
        "category": "technology",
        "timestamp": datetime(2025, 7, 17, 10, 15),
        "is_breaking": False
    }
]

@app.route("/news")
def show_news():
    return render_template("news.html", news=news_list)

if __name__ == "__main__":
    app.run(debug=True)
