from flask import Flask

app = Flask(__name__)


# 10. Language validation
@app.route('/language/<lang>')
def language_check(lang):
    valid_langs = ['python', 'java', 'c++', 'javascript']
    if lang.lower() in valid_langs:
        return f"{lang} is a supported language."
    else:
        return f"{lang} is not supported."


if __name__ == '__main__':
    app.run(debug=True)
