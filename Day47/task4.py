from flask import Flask

app = Flask(__name__)



# 4. Status update simulation
@app.route('/status/<username>/<status>')
def user_status(username, status):
    return f"User '{username}' updated their status to: '{status}'"



if __name__ == '__main__':
    app.run(debug=True)
