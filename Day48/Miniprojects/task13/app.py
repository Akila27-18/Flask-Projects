from flask import Flask, render_template

app = Flask(__name__)

@app.route('/testimonials')
def testimonials():
    feedbacks = [
        {
            'name': 'Aanya Kapoor',
            'comment': 'This service exceeded my expectations. Very responsive and professional!',
            'photo': 'user1.jpg',
            'rating': 5
        },
        {
            'name': 'Rohan Mehta',
            'comment': 'Good experience overall, but there’s room for improvement.',
            'photo': 'user2.jpg',
            'rating': 3
        },
        {
            'name': 'Priya Das',
            'comment': 'Amazing support and easy to use. Highly recommended!',
            'photo': 'user3.jpg',
            'rating': 4
        }
    ]
    return render_template('testimonials.html', testimonials=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
