from flask import Flask

app = Flask(__name__)



# 12. Country code to full name
@app.route('/country/<code>')
def country_name(code):
    countries = {
        'in': 'India',
        'us': 'United States',
        'uk': 'United Kingdom',
        'jp': 'Japan'
    }
    return countries.get(code.lower(), "Unknown country code")


if __name__ == '__main__':
    app.run(debug=True)
