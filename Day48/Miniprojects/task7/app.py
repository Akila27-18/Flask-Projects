from flask import Flask, render_template

app = Flask(__name__)

@app.route("/menu")
def menu():
    menu_data = {
        "Starters": [
            {"name": "Tomato Soup", "image": "soup.jpg", "available": True},
            {"name": "Garlic Bread", "image": "garlic_bread.jpg", "available": False},
        ],
        "Main Course": [
            {"name": "Grilled Steak", "image": "steak.jpg", "available": True},
            {"name": "Veg Lasagna", "image": "lasagna.jpg", "available": True},
        ],
        "Desserts": [
            {"name": "Chocolate Cake", "image": "cake.jpg", "available": False},
            {"name": "Ice Cream", "image": "ice_cream.jpg", "available": True},
        ]
    }
    return render_template("menu.html", menu=menu_data)

if __name__ == "__main__":
    app.run(debug=True)
