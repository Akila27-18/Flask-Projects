from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory store for ratings
ratings = []

@app.route('/rate', methods=['GET'])
def rate_form():
    return render_template('rate_form.html')

@app.route('/submit-rating', methods=['POST'])
def submit_rating():
    name = request.form.get('name')
    movie = request.form.get('movie')
    rating = request.form.get('rating')

    # Store entry
    ratings.append({'name': name, 'movie': movie, 'rating': rating})
    return redirect(url_for('thank_you', name=name))

@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)

@app.route('/ratings')
def all_ratings():
    movie_filter = request.args.get('movie')
    if movie_filter:
        filtered = [r for r in ratings if r['movie'].lower() == movie_filter.lower()]
    else:
        filtered = ratings
    return render_template('ratings.html', ratings=filtered, filter=movie_filter)

@app.route('/movie/<title>')
def movie_page(title):
    return f"<h2>Movie Info: {title.title()}</h2><p>This is a page for the movie '{title.title()}'.</p>"
