from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return redirect(url_for('thankyou'))
    return '''
    <form method="post">
        <input name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/thankyou')
def thankyou():
    return "Thank you for your submission!"

if __name__ == "__main__":
    app.run(debug=True)
