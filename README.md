
# 📊 Variance Analysis FP&A Tool

A simple and interactive variance analysis dashboard built with **Streamlit**, designed for FP&A teams, analysts, and finance professionals.

> Upload budget vs. actual financials and get an instant breakdown of variances in both dollar and percentage terms — with visual insights.

---

## 🚀 Features

- Upload CSV with Budget vs. Actuals
- Auto-calculates:
  - 🔸 Variance ($)
  - 🔸 Variance (%)
  - 🔸 Direction (Increase / Decrease)
- Bar chart highlighting top variances
- Downloadable results

---

## 📂 Sample Input Format

| Category  | Budget   | Actual   |
|-----------|----------|----------|
| Revenue   | 1000000  | 920000   |
| COGS      | 400000   | 390000   |
| SG&A      | 200000   | 215000   |

---

## 🛠️ How to Run

1. Clone the repo  
2. (Optional) Set up a virtual environment  
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run variance_dashboard.py
```

---

## 📦 Tech Stack

- Python 🐍
- Streamlit 🌐
- Pandas
- Matplotlib

---

## 📥 Sample Data

You can use the included `financials_demo.csv` to test the tool right away.

---

## 🤝 Contributions

Pull requests and ideas are welcome — let’s make finance more automated and insightful.

---

## 📄 License

MIT License
