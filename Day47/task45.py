from flask import Flask, request

app = Flask(__name__)

@app.route('/showdata', methods=['GET', 'POST'])
def show_data():
    if request.method == 'POST':
        form_data = dict(request.form)
        return f"<pre>{form_data}</pre>"
    return '''
    <form method="post">
        Name: <input name="name"><br>
        Age: <input name="age"><br>
        <button type="submit">Send</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
