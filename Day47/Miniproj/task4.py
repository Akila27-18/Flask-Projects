from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory vote storage
votes = {}  # {name: option}

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    return '''
    <h2>Simple Online Poll</h2>
    <form method="POST" action="/vote">
      Name: <input type="text" name="name" required><br><br>
      Choose an option:<br>
      <input type="radio" name="option" value="A" required> Option A<br>
      <input type="radio" name="option" value="B"> Option B<br>
      <input type="radio" name="option" value="C"> Option C<br><br>
      <input type="submit" value="Vote">
    </form>
    '''

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form.get('name')
    option = request.form.get('option')

    if name and option:
        votes[name] = option
        return redirect(url_for('result', option=option))
    return "Missing name or option", 400

@app.route('/result')
def result():
    selected_option = request.args.get('option')
    if selected_option not in ['A', 'B', 'C']:
        return "Invalid or missing option", 400

    count = sum(1 for v in votes.values() if v == selected_option)
    return f"<h2>Results</h2><p>Votes for Option {selected_option}: <strong>{count}</strong></p>"

@app.route('/voter/<name>')
def voter(name):
    option = votes.get(name)
    if option:
        return f"<h2>Hi {name}!</h2><p>You voted for Option <strong>{option}</strong>.</p>"
    else:
        return f"<h2>{name}</h2><p>No vote recorded.</p>"

if __name__ == '__main__':
    app.run(debug=True)
