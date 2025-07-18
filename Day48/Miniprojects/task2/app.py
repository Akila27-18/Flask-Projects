from flask import Flask, render_template

app = Flask(__name__)

@app.route("/books")
def show_books():
    books = [
        {"name": "The Alchemist", "author": "Paulo Coelho", "image": "book1.jpg"},
        {"name": "1984", "author": "George Orwell", "image": "book2.jpg"}
        # Add or remove items to test empty list
    ]
    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
