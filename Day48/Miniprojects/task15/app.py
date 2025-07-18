from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/achievements')
def achievements():
    current_year = datetime.now().year
    data = {
        2023: ["Won National Tech Award", "Launched New Product Line"],
        2024: ["Expanded to 3 Countries", "Hit 1M Customers"],
        2025: ["Opened AI R&D Center", "Partnered with SpaceX"]
    }
    return render_template("achievements.html", data=data, current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
