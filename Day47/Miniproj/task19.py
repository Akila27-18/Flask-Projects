from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Dummy weather data
weather_data = {
    'chennai': {'temp_c': 34, 'desc': 'Sunny'},
    'delhi': {'temp_c': 36, 'desc': 'Hot and Dry'},
    'mumbai': {'temp_c': 30, 'desc': 'Humid with clouds'}
}

@app.route('/weather')
def weather_form():
    unit = request.args.get('unit', 'celsius')  # default unit
    return f'''
    <h2>Weather Report Generator</h2>
    <form method="POST" action="/weather-result">
        Enter City: <input type="text" name="city" required><br><br>
        <input type="hidden" name="unit" value="{unit}">
        <input type="submit" value="Get Weather">
    </form>
    <p>Current Unit: <strong>{unit.capitalize()}</strong></p>
    <p>Switch Unit: <a href="/weather?unit=metric">Metric</a> | <a href="/weather?unit=imperial">Imperial</a></p>
    '''

@app.route('/weather-result', methods=['POST'])
def weather_result():
    city = request.form.get('city').lower()
    unit = request.form.get('unit')
    return redirect(url_for('weather_report', city=city, unit=unit))

@app.route('/weather/<city>')
def weather_report(city):
    unit = request.args.get('unit', 'celsius')
    city = city.lower()

    if city not in weather_data:
        return f"<h2>No data for {city.title()}</h2><p>Please try another city.</p>"

    info = weather_data[city]
    temp_c = info['temp_c']
    desc = info['desc']

    if unit == 'imperial':
        temp = round((temp_c * 9/5) + 32)
        unit_label = '°F'
    else:
        temp = temp_c
        unit_label = '°C'

    return f'''
    <h2>Weather in {city.title()}</h2>
    <p>Description: {desc}</p>
    <p>Temperature: {temp}{unit_label}</p>
    <a href="/weather?unit={unit}">Check Another City</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
