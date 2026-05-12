# 💰 Finance Manager AI

<div align="center">

**A smart personal finance management web application with AI-powered insights, budget tracking, and financial analytics.**

</div>

---

## 📖 About

Finance Manager AI is a powerful personal finance management web application designed to help users take control of their money. Whether you're tracking daily expenses, monitoring spending patterns, or working towards financial goals, this app provides intelligent insights and visual analytics to make better financial decisions.

**Track where your money goes, understand your spending habits, and achieve your financial goals!**

---

## ✨ Key Features

- 💵 **Expense Tracking** — Easily log income and expenses with detailed descriptions
- 🏷️ **Smart Categorization** — Automatically categorize transactions (Food, Transport, Utilities, etc.)
- 📊 **Visual Analytics** — Beautiful charts and graphs showing spending patterns
- 🎯 **Budget Management** — Set budgets for different categories and track progress
- 🚨 **Smart Alerts** — Get notified when you exceed budget limits
- 📈 **Financial Reports** — Generate detailed reports of your income vs expenses
- 💾 **Data Persistence** — All data securely stored and synced
- 🌙 **Responsive Design** — Works perfectly on desktop, tablet, and mobile devices

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python, Flask |
| **Database** | SQLite / PostgreSQL |
| **Charts** | Chart.js / Matplotlib |
| **Deployment** | Render.com |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
Finance-Manager-AI/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml            # Render deployment config
├── templates/             # HTML templates
│   ├── index.html
│   ├── dashboard.html
│   ├── add_expense.html
│   └── reports.html
├── static/                # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python** 3.8 or higher
- **pip** (Python package manager)
- **Git**
- A modern web browser

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Dhanush153212/Finance-Manager-AI.git
   cd Finance-Manager-AI
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   ```
   Open your browser and go to: http://localhost:5000
   ```

---

## 📝 Usage

### Adding an Expense

1. Click **"Add Expense"** button
2. Fill in the transaction details:
   - Amount
   - Category (Food, Transport, Entertainment, etc.)
   - Date
   - Description
3. Click **"Save"** to record the transaction

### Viewing Dashboard

- See your **total balance** at a glance
- View **expense breakdown** by category
- Monitor **budget vs actual spending**
- Check **recent transactions**

### Setting Budgets

1. Go to **"Budget Settings"**
2. Set monthly budget for each category
3. Get alerts when approaching the limit

### Generating Reports

1. Navigate to **"Reports"**
2. Select **date range** and **categories**
3. View detailed analysis and download reports

---

## 📚 Configuration

### Environment Variables

Create a `.env` file in the root directory (optional):

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Database
DATABASE_URL=sqlite:///finance.db

# Security (if using authentication)
SECRET_KEY=your_secret_key_here
```

### Database Setup

The app uses SQLite by default. On first run:

```bash
python app.py
# Database will auto-initialize
```

---

## 📊 Features in Detail

### Dashboard Overview
- **Balance Display** — Current account balance
- **Spending Summary** — Total expenses this month
- **Income Summary** — Total income this month
- **Category Breakdown** — Pie chart showing spending distribution
- **Recent Transactions** — Latest 5 transactions

### Budget Alerts

Smart rule-based alerts notify you when:
- Monthly budget for a category is 80% spent
- A single transaction exceeds set limit
- Monthly budget is exceeded

### Financial Analytics

Visual charts include:
- **Pie Charts** — Spending by category
- **Bar Charts** — Monthly comparison
- **Line Charts** — Spending trends
- **Statistical Reports** — Average spending per category

---

## 🚀 Deployment

### Deploy to Render

1. **Push your code to GitHub**
2. **Connect your repo to Render**:
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect GitHub repository
3. **Set Environment Variables**
4. **Deploy** — Render will automatically build and deploy

The `render.yaml` file is already configured for deployment.

## 🧪 Testing

Run tests (if available):

```bash
# Using pytest
pytest

# With coverage
pytest --cov=app
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Run on different port
python app.py --port 5001
```

### Database Issues
```bash
# Reset database (be careful!)
rm instance/finance.db
python app.py  # Will recreate database
```

### Dependencies Error
```bash
# Upgrade pip first
pip install --upgrade pip

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Import Errors
```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

---

## 📈 Roadmap

- [x] Basic expense tracking
- [x] Budget management
- [x] Visual analytics & charts
- [x] Alert system
- [ ] User authentication & accounts
- [ ] Multiple wallet support
- [ ] AI spending recommendations
- [ ] Mobile app
- [ ] Cloud sync
- [ ] Export to PDF/Excel
- [ ] Multi-currency support

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/Dhanush153212/Finance-Manager-AI.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Write clean, readable code
   - Add comments where necessary
   - Test your changes

4. **Commit Your Changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```

5. **Push to the Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Describe your changes clearly
   - Link related issues
   - Wait for review

---

## 🔒 Security

- ✅ Input validation on all forms
- ✅ Secure session management
- ✅ CSRF protection enabled
- ✅ Sensitive data not logged
- ✅ Regular dependency updates

**Note:** This is a personal project. For production use, add authentication and encryption.

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) file for details.

---

## 💬 Support & Contact

- **GitHub Issues** — [Report bugs or request features](https://github.com/Dhanush153212/Finance-Manager-AI/issues)
- **Email** — Reach out for questions or collaboration

---

## 👤 Author

**Dhanush.C** (Dhanush153212)

- 🐙 **GitHub** — [@Dhanush153212](https://github.com/Dhanush153212)
- 💼 **About** — CS Student | Building Real Projects | AI, Backend, Automation
- **Tech Stack** — Python | Java | Git

---

## 🙏 Acknowledgments

- Built with Python & Flask
- Charts powered by Chart.js
- Deployed on Render.com
- Thanks to the open-source community

---

<div align="center">

### ⭐ If you found this helpful, please give it a star!

**[⬆ Back to Top](#-finance-manager-ai)**

Made with ❤️ by [Dhanush.C](https://github.com/Dhanush153212)

</div>
