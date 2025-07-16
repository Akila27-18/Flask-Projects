from flask import Flask, request

app = Flask(__name__)

@app.route('/contact', methods=['GET'])
def contact():
    return '''
    <form method="post" action="/thankyou">
        <input name="name"><br>
        <textarea name="message"></textarea><br>
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/thankyou', methods=['POST'])
def thankyou():
    name = request.form['name']
    return f"Thank you, {name}, for your message!"

if __name__ == "__main__":
    app.run(debug=True)
