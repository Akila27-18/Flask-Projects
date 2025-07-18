from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blogs')
def blogs():
    blog_list = [
        {
            'title': 'The Future of AI',
            'author': 'Arjun Menon',
            'snippet': 'Artificial Intelligence is transforming industries at a rapid pace...',
            'image': 'images/blog1.jpg',
            'featured': True
        },
        {
            'title': 'Travel Tips for 2025',
            'author': 'Meera Iyer',
            'snippet': 'Planning a vacation? Here’s what you need to know before booking...',
            'image': 'images/blog2.jpg',
            'featured': False
        },
        {
            'title': 'Mastering Python in 30 Days',
            'author': 'Ravi Kumar',
            'snippet': 'Python is easy to learn and extremely powerful. This guide breaks it down...',
            'image': 'images/blog3.jpg',
            'featured': True
        }
    ]

    return render_template('blogs.html', blogs=blog_list)

if __name__ == '__main__':
    app.run(debug=True)
