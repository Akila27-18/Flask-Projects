from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    time = request.args.get('time', 'day')
    return f"<h2>Good {time.capitalize()}, {name}!</h2>"

@app.route('/custom-greet/<name>')
def custom_greet(name):
    return f"<h2>Hello {name}, welcome to our greeting service!</h2>"

@app.route('/greet-form')
def greet_form():
    return '''
    <h2>Enter Your Name and Time of Day</h2>
    <form action="/submit-greet" method="POST">
        Name: <input type="text" name="name" required><br><br>
        Time of Day: 
        <select name="time">
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
            <option value="night">Night</option>
        </select><br><br>
        <button type="submit">Generate Greeting</button>
    </form>
    '''

@app.route('/submit-greet', methods=['POST'])
def submit_greet():
    name = request.form['name']
    time = request.form['time']
    return redirect(url_for('greet_result', name=name, time=time))

@app.route('/greet-result')
def greet_result():
    name = request.args.get('name', 'Guest')
    time = request.args.get('time', 'day')
    return f"<h2>Greeting Result:</h2><p>Good {time.capitalize()}, {name}!</p>"

if __name__ == '__main__':
    app.run(debug=True)
