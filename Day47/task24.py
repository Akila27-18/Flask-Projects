from flask import Flask, request

app = Flask(__name__)

@app.route('/button', methods=['GET', 'POST'])
def button():
    if request.method == 'POST':
        return "Button pressed! POST request received."
    return '''
    <form method="post">
        <button type="submit">Click Me</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
