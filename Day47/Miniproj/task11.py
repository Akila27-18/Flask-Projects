from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory list to store scores
leaderboard = []

# Route 1: Quiz Form
@app.route('/quiz', methods=['GET'])
def quiz_form():
    return render_template_string("""
        <h2>Student Quiz</h2>
        <form method="post" action="{{ url_for('quiz_result') }}">
            Name: <input type="text" name="name" required><br><br>

            <p>1. What is the capital of France?</p>
            <input type="radio" name="q1" value="Paris" required> Paris<br>
            <input type="radio" name="q1" value="London"> London<br>
            <input type="radio" name="q1" value="Berlin"> Berlin<br><br>

            <p>2. 5 + 7 = ?</p>
            <input type="radio" name="q2" value="10" required> 10<br>
            <input type="radio" name="q2" value="12"> 12<br>
            <input type="radio" name="q2" value="14"> 14<br><br>

            <p>3. Who wrote Hamlet?</p>
            <input type="radio" name="q3" value="Shakespeare" required> Shakespeare<br>
            <input type="radio" name="q3" value="Hemingway"> Hemingway<br>
            <input type="radio" name="q3" value="Tolkien"> Tolkien<br><br>

            <button type="submit">Submit Quiz</button>
        </form>
    """)

# Route 2: Handle Quiz POST and Redirect
@app.route('/quiz-result', methods=['POST'])
def quiz_result():
    name = request.form['name']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']

    # Simple answer key
    score = 0
    if q1 == "Paris": score += 1
    if q2 == "12": score += 1
    if q3 == "Shakespeare": score += 1

    leaderboard.append({'name': name, 'score': score})
    return redirect(url_for('quiz_summary', name=name))

# Route 3: Show Quiz Summary (Dynamic)
@app.route('/quiz-summary/<name>')
def quiz_summary(name):
    # Find the latest score of the student
    user_data = next((entry for entry in reversed(leaderboard) if entry['name'] == name), None)
    if not user_data:
        return f"<h3>No results found for {name}.</h3>"

    return f"""
        <h2>Quiz Summary for {name}</h2>
        <p>Your score: {user_data['score']} / 3</p>
    """

# Route 4: Leaderboard with score filter
@app.route('/leaderboard')
def show_leaderboard():
    score_filter = request.args.get('score')
    if score_filter:
        try:
            score_filter = int(score_filter)
            filtered = [entry for entry in leaderboard if entry['score'] == score_filter]
        except:
            return "<h3>Invalid score filter.</h3>"
    else:
        filtered = leaderboard

    html = "<h2>Leaderboard</h2><ul>"
    for entry in filtered:
        html += f"<li>{entry['name']} - {entry['score']}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
