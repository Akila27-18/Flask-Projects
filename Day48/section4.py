from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 1. Route to pass name to template
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# 2. Pass list of courses
@app.route('/courses')
def courses():
    course_list = ['Python', 'JavaScript', 'HTML', 'CSS']
    return render_template('courses.html', courses=course_list)

# 3. Boolean flag for login status
@app.route('/auth')
def auth():
    is_logged_in = True  # or False
    return render_template('auth.html', is_logged_in=is_logged_in)

# 4. Dictionary as user profile
@app.route('/profile')
def profile():
    user_profile = {
        'name': 'Arjun',
        'email': 'arjun@example.com',
        'age': 30
    }
    return render_template('profile.html', profile=user_profile)

# 5. Pass current date and time
@app.route('/datetime')
def show_datetime():
    current_time = datetime.now()
    return render_template('datetime.html', time=current_time)

# 6. Pass news items list
@app.route('/news')
def news():
    news_items = ['Stock market hits record high', 'New species discovered', 'Flask 3.0 released']
    return render_template('news.html', news_items=news_items)

# 7. Pass multiple variables
@app.route('/profile-card')
def profile_card():
    return render_template('profile_card.html', name='Anita', age=25, city='Chennai')

# 8. Send dynamic title
@app.route('/dynamic-title/<page>')
def dynamic_title(page):
    title = f"{page.capitalize()} - My Site"
    return render_template('dynamic_title.html', title=title)

# 9. Loop through list of product dicts
@app.route('/products')
def products():
    products = [
        {'name': 'Laptop', 'price': 70000},
        {'name': 'Phone', 'price': 30000},
        {'name': 'Tablet', 'price': 25000},
    ]
    return render_template('products.html', products=products)

# 10. Compute tax and pass it
@app.route('/tax')
def tax():
    amount = 1000
    tax_rate = 0.18
    tax = amount * tax_rate
    total = amount + tax
    return render_template('tax.html', amount=amount, tax=tax, total=total)

if __name__ == '__main__':
    app.run(debug=True)
