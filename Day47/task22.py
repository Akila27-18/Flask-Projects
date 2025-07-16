from flask import Flask, request

app = Flask(__name__)

@app.route('/check', methods=['GET', 'POST'])
def check():
    print(f"Request method is: {request.method}")
    return f"Method is {request.method}"

if __name__ == "__main__":
    app.run(debug=True)
