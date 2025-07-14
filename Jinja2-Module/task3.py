from jinja2 import Environment, FileSystemLoader
from datetime import date
import os

# 1. Set up Jinja2 environment (loads templates from current dir)
env = Environment(loader=FileSystemLoader(searchpath="./"))

# 2. Load the template
template = env.get_template("email_template.txt")

# 3. Define user data
user_data = {
    "name": "Akila Sharma",
    "product": "Premium Budget Tracker",
    "date": date.today().strftime("%B %d, %Y")
}

# 4. Render email body
email_body = template.render(user_data)

# 5. Output to console or save
print("📧 Generated Email:\n")
print(email_body)

# Optional: Save to file
with open("output_email.txt", "w", encoding="utf-8") as f:
    f.write(email_body)
print("\n✅ Saved to 'output_email.txt'")
