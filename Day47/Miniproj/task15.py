from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store goals
goals = []

@app.route('/goal', methods=['GET'])
def goal_form():
    return render_template('goal_form.html')

@app.route('/goal-submit', methods=['POST'])
def goal_submit():
    name = request.form.get('name')
    goal = request.form.get('goal')

    # Save to in-memory list
    goals.append({'name': name, 'goal': goal})

    return redirect(url_for('goal_status', name=name))

@app.route('/goal-status/<name>')
def goal_status(name):
    user_goals = [g for g in goals if g['name'].lower() == name.lower()]
    return render_template('goal_status.html', name=name, user_goals=user_goals)

@app.route('/goals')
def all_goals():
    goal_type = request.args.get('type')
    if goal_type:
        filtered = [g for g in goals if goal_type.lower() in g['goal'].lower()]
    else:
        filtered = goals
    return render_template('goal_list.html', goals=filtered, filter_type=goal_type)
