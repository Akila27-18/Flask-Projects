from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {"title": "Inception", "poster": "movie1.jpg", "new": False},
    {"title": "Oppenheimer", "poster": "movie2.jpg", "new": True},
    {"title": "The Matrix", "poster": "movie3.jpg", "new": False},
    {"title": "Inside Out 2", "poster": "movie4.jpg", "new": True}
]

@app.route("/movies")
def show_movies():
    return render_template("movies.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
