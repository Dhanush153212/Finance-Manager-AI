from flask import Flask, render_template, request,redirect, url_for
import sqlite3
import os
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount INTEGER,
        category TEXT,
        date TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS budgets(
        category TEXT PRIMARY KEY,
        budget_limit INTEGER
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            category TEXT
        )
    """)

    # Category totals
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cur.fetchall()

    # All expenses
    cur.execute("SELECT id, amount, category FROM expenses")
    expenses = cur.fetchall()

    conn.close()

    total_spent = sum(row[1] for row in data)

    advice = ""

    return render_template(
        "index.html",
        data=data,
        expenses=expenses,
        total=total_spent,
        advice=advice
    )

@app.route("/edit", methods=["POST"])
def edit_expense():
    id = request.form["id"]
    amount = request.form["amount"]
    category = request.form["category"]
    date = request.form["date"]
    
@app.route("/delete", methods=["POST"])
def delete_expense():
    id = request.form["id"]

    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE expenses SET amount=?, category=? WHERE id=?",
        (amount, category, id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

@app.route("/set-budget", methods=["POST"])
def set_budget():
    category = request.form["category"].lower()
    budget_limit = int(request.form["budget_limit"])

    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO expenses (category, amount, date)
        VALUES (?, ?, ?)
    """, (category, budget_limit))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port,debug=False)