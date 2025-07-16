from flask import Flask

app = Flask(__name__)



# 15. Error handling route
@app.route('/error/<int:code>')
def error_route(code):
    errors = {
        404: "Page not found",
        403: "Forbidden access",
        500: "Internal server error"
    }
    return errors.get(code, "Unknown error code")

if __name__ == '__main__':
    app.run(debug=True)
