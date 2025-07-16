from flask import Flask, request, redirect, url_for, render_template_string
import urllib.parse

app = Flask(__name__)

# In-memory book database
book_data = [
    {'title': 'Dune', 'genre': 'sci-fi', 'desc': 'Epic sci-fi adventure on desert planet.'},
    {'title': 'Neuromancer', 'genre': 'sci-fi', 'desc': 'Cyberpunk classic by William Gibson.'},
    {'title': 'Pride and Prejudice', 'genre': 'romance', 'desc': 'Timeless romance by Jane Austen.'},
    {'title': 'The Notebook', 'genre': 'romance', 'desc': 'Emotional love story by Nicholas Sparks.'}
]

# HTML form template
form_html = '''
<!DOCTYPE html>
<html>
<head><title>Book Recommendation</title></head>
<body>
  <h2>Get a Book Recommendation</h2>
  <form method="POST" action="/show-recommendation">
    Name: <input type="text" name="user" required><br><br>
    Choose Genre:
    <select name="genre">
      <option value="sci-fi">Sci-Fi</option>
      <option value="romance">Romance</option>
    </select><br><br>
    <button type="submit">Get Recommendation</button>
  </form>
</body>
</html>
'''

# Show recommendation form
@app.route('/recommend')
def recommend():
    return form_html

# Handle form and redirect
@app.route('/show-recommendation', methods=['POST'])
def show_recommendation():
    user = request.form['user']
    genre = request.form['genre']

    # Optional: Store or log the recommendation request here
    return redirect(url_for('thanks', user=user))

# Thank-you route
@app.route('/thanks/<user>')
def thanks(user):
    return f"<h2>Thank you, {user}! Check /books?genre=your_choice for recommendations.</h2>"

# List books by genre
@app.route('/books')
def book_list():
    genre = request.args.get('genre')
    filtered = [b for b in book_data if b['genre'] == genre] if genre else book_data

    html = f"<h2>Books in genre: {genre}</h2><ul>"
    for book in filtered:
        safe_title = urllib.parse.quote(book['title'])
        html += f"<li><a href='/book/{safe_title}'>{book['title']}</a></li>"
    html += "</ul>"
    return html

# Show details of individual book
@app.route('/book/<title>')
def book_detail(title):
    decoded_title = urllib.parse.unquote(title)
    book = next((b for b in book_data if b['title'].lower() == decoded_title.lower()), None)
    if book:
        return f"""
        <h2>{book['title']}</h2>
        <p><strong>Genre:</strong> {book['genre'].title()}</p>
        <p><strong>Description:</strong> {book['desc']}</p>
        """
    else:
        return "<h3>Book not found.</h3>"

if __name__ == '__main__':
    app.run(debug=True)
