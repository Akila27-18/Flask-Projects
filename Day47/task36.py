from flask import Flask

app = Flask(__name__)

@app.route('/contact', methods=['GET'])
def contact():
    return '''
    <form method="post" action="/thankyou">
        Name: <input name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <button type="submit">Send</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
