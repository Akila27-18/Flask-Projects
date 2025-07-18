from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# Simulated user database
users = {
    "alice": {
        "name": "Alice Johnson",
        "bio": "Frontend developer and UI/UX enthusiast.",
        "joined": datetime.today() - timedelta(days=3),
        "image": "alice.jpg"
    },
    "bob": {
        "name": "Bob Smith",
        "bio": "Data scientist with a passion for machine learning.",
        "joined": datetime.today() - timedelta(days=30),
        "image": "bob.jpg"
    }
}

@app.route("/profile/<username>")
def profile(username):
    user = users.get(username)
    if not user:
        return "User not found", 404

    # Check if user joined within the last 7 days
    is_new = (datetime.today() - user["joined"]).days < 7

    return render_template("profile.html",
                           name=user["name"],
                           bio=user["bio"],
                           joined=user["joined"].strftime("%B %d, %Y"),
                           image=user["image"],
                           is_new=is_new)

if __name__ == "__main__":
    app.run(debug=True)
