from flask import Flask

app = Flask(__name__)

@app.route('/feedback', methods=['GET'])
def feedback():
    return '''
    <form method="post" action="/submit-feedback">
        <textarea name="message" placeholder="Your feedback..."></textarea>
        <br>
        <button type="submit">Submit Feedback</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
