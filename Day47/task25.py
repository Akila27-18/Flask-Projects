from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return f"POST data received: {request.form.get('data')}"
    elif request.method == 'GET' and 'data' in request.args:
        return f"GET data received: {request.args.get('data')}"
    return '''
    <form method="get">
        <input name="data" placeholder="Try GET">
        <button type="submit">Submit GET</button>
    </form>
    <br>
    <form method="post">
        <input name="data" placeholder="Try POST">
        <button type="submit">Submit POST</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
