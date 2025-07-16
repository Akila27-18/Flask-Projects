from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory mood log
mood_entries = []

@app.route('/log-mood', methods=['GET'])
def log_mood():
    return render_template('log_mood.html')

@app.route('/mood-result', methods=['POST'])
def mood_result():
    name = request.form.get('name')
    mood = request.form.get('mood')
    reason = request.form.get('reason')

    # Store entry
    mood_entries.append({'name': name, 'mood': mood, 'reason': reason})

    return redirect(url_for('thank_you', name=name))

@app.route('/logs')
def show_logs():
    mood_filter = request.args.get('mood')
    if mood_filter:
        filtered = [entry for entry in mood_entries if entry['mood'].lower() == mood_filter.lower()]
    else:
        filtered = mood_entries

    return render_template('mood_logs.html', entries=filtered, filter=mood_filter)

@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)
