from flask import Flask

app = Flask(__name__)

# 13. Debug print
@app.route('/debug/<param>')
def debug_route(param):
    print(f"[DEBUG] Received param: {param}")
    return f"Check the console. Received param: {param}"


if __name__ == '__main__':
    app.run(debug=True)
