from jinja2 import Template

# 1. Load the Jinja2 template
with open("template.html", "r", encoding="utf-8") as f:
    template_str = f.read()
template = Template(template_str)

# 2. Define your data
data = {
    "title": "My Portfolio",
    "name": "Akila Sharma",
    "bio": "Passionate developer and designer.",
    "projects": [
        {"name": "Weather App", "desc": "Real-time weather updates using API."},
        {"name": "Budget Tracker", "desc": "Track your monthly expenses."},
        {"name": "Stock Viewer", "desc": "Monitor stock prices live."}
    ],
    "show_contact": True,
    "email": "akila@example.com"
}

# 3. Render the template with data
rendered_html = template.render(data)

# 4. Save to output HTML file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("✅ Static website generated as 'output.html'")
