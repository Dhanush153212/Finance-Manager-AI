from flask import Flask, render_template, request,redirect, url_for
import sqlite3
import os
app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category"
    )
    data = cur.fetchall()

    total_spent = sum(row[1] for row in data)

    food = 0
    investment = 0

    for category, amount in data:
        if category.lower() == "food":
            food = amount
        if category.lower() == "investment":
            investment = amount

    advice = ""

    if total_spent > 0:
        if food / total_spent > 0.5:
            advice = "You are spending more than 50% on food. Try to reduce expenses."
        elif investment / total_spent < 0.2:
            advice = "Your investment is less than 20%. Consider investing more."

    conn.close()

    return render_template(
        "index.html",
        data=data,
        total=total_spent,
        advice=advice
    )
@app.route("/add", methods=["POST"])
def add_expense():
    amount = int(request.form["amount"])
    category = request.form["category"]

    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS expenses (amount INT, category TEXT)"
    )
    cur.execute(
        "INSERT INTO expenses VALUES (?, ?)",
        (amount, category)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port,debug=False)