from jinja2 import Template
from datetime import date

# 1. Load template
with open("invoice_template.html", "r", encoding="utf-8") as file:
    template = Template(file.read())

# 2. Define invoice data
invoice_data = {
    "invoice_no": "INV-1001",
    "date": date.today().strftime("%Y-%m-%d"),
    "client": "Akila Sharma",
    "items": [
        {"name": "Web Design", "desc": "Homepage + contact page", "qty": 1, "price": 5000},
        {"name": "SEO Service", "desc": "3 months SEO optimization", "qty": 1, "price": 3000},
        {"name": "Hosting", "desc": "1 year shared hosting", "qty": 1, "price": 1200}
    ]
}

# 3. Calculate total
invoice_data["total"] = sum(item["qty"] * item["price"] for item in invoice_data["items"])

# 4. Render HTML
rendered = template.render(invoice_data)

# 5. Save output
with open("invoice_output.html", "w", encoding="utf-8") as f:
    f.write(rendered)

print("✅ Invoice generated: invoice_output.html")
