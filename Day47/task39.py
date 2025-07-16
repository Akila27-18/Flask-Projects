from flask import Flask, request

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        if not name or not message:
            return "Error: All fields are required."
        return f"Thanks {name}, message received!"
    return '''
    <form method="post">
        Name: <input name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <button type="submit">Submit</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
