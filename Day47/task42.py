from flask import Flask, request

app = Flask(__name__)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        rating = request.form.get('rating')
        return f"Thanks for your rating: {rating}/5"
    return '''
    <form method="post">
        Rate us (1–5): <select name="rating">
            <option>1</option><option>2</option><option>3</option>
            <option>4</option><option>5</option>
        </select><br>
        <button type="submit">Submit</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
