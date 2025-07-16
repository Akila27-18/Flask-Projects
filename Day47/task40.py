from flask import Flask, request

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        msg = request.form.get('message')
        return f"""
        <div style="border:1px solid #ccc; padding:10px;">
            <h2>Thank You, {name}!</h2>
            <p>Your message:</p>
            <blockquote>{msg}</blockquote>
        </div>
        """
    return '''
    <form method="post">
        Name: <input name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <button type="submit">Send</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
