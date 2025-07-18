from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/weather')
def weather():
    # Dummy data for demonstration
    weather_data = {
        'date': datetime.date.today().strftime('%B %d, %Y'),
        'temperature': 33,
        'condition': 'sun',  # use 'rain' or 'sun'
        'hourly_temps': [26, 28, 30, 32, 33, 31, 29]
    }
    return render_template('weather.html', **weather_data)

if __name__ == '__main__':
    app.run(debug=True)
