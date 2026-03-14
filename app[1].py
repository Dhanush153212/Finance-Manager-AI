from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# v2 forces a fresh DB with correct schema
DB_PATH = "/tmp/finance_v2.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS expenses")
    cur.execute("DROP TABLE IF EXISTS budgets")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            date TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            category TEXT PRIMARY KEY,
            budget_limit REAL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category ORDER BY total DESC")
        data = cur.fetchall()
        cur.execute("SELECT id, amount, category, date FROM expenses ORDER BY date DESC")
        expenses = cur.fetchall()
        conn.close()

        total_spent = sum(row["total"] for row in data)

        advice = ""
        if data:
            top_cat = data[0]
            pct = round((top_cat["total"] / total_spent) * 100) if total_spent else 0
            if pct > 50:
                advice = f"You've spent {pct}% on {top_cat['category']}. Consider reducing this to balance your budget."
            else:
                advice = "Great job! Keep tracking your expenses to spot savings opportunities."

        return render_template("index.html", data=data, expenses=expenses, total=total_spent, advice=advice)
    except Exception as e:
        return f"<h2>Error: {str(e)}</h2>", 500

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form.get("amount", type=float)
    category = request.form.get("category", "Other")
    date = request.form.get("date")
    if amount and amount > 0 and date:
        conn = get_db()
        conn.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, date))
        conn.commit()
        conn.close()
    return redirect(url_for("home"))

@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    conn = get_db()
    conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
