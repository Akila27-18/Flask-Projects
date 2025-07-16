from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword:
        return f"Keyword: {keyword}"
    return "No keyword found"

if __name__ == '__main__':
    app.run(debug=True)
