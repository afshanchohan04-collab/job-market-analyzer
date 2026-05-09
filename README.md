# 📊 Job Market Data Analyzer — Python + SQL + Data Visualization

A data analysis project that explores real-world job market trends using salary and employment data. Covers the full data pipeline: raw data ingestion, cleaning, SQL storage, analysis, and visualization.

---

## 📌 Project Overview

This project answers key questions about the modern data job market:
- Which roles are most in demand?
- How do salaries vary by experience level?
- How prevalent is remote work?
- Which locations offer the most opportunities?

Using Python and SQLite, data is cleaned, stored relationally, queried with SQL, and visualized using Matplotlib charts — reflecting a real-world data analyst workflow.

---

## ✨ Key Insights from the Data

| Finding | Result |
|---|---|
| 🏆 Most Common Roles | Data Scientist, Data Engineer |
| 💰 Highest Salaries | Executive-level positions |
| 🌍 Remote Work | Majority of roles are fully remote |
| 📍 Top Location | United States leads in job volume |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Data Analysis:** Pandas
- **Database:** SQLite3
- **Visualization:** Matplotlib
- **Data Format:** CSV (real-world dataset)

---

## 📂 Project Structure

```
job-market-analyzer/
│
├── data/                  # Raw and cleaned dataset files
├── scripts/
│   ├── data_cleaning.py   # Data preprocessing and null handling
│   ├── analysis.py        # SQL queries and statistical analysis
│   └── db_setup.py        # SQLite database creation and loading
├── visuals/               # Generated charts and plots
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/afshan-chohan/job-market-analyzer.git
cd job-market-analyzer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run scripts in order**
```bash
# Step 1: Clean the raw data
python scripts/data_cleaning.py

# Step 2: Set up the SQLite database and load data
python scripts/db_setup.py

# Step 3: Run analysis and generate visualizations
python scripts/analysis.py
```

---

## 🔍 Analysis Performed

### 1. Data Cleaning
- Handled missing and null values
- Standardised column formats
- Removed duplicates and irrelevant entries

### 2. SQL-Based Analysis
```sql
-- Top job roles by frequency
SELECT job_title, COUNT(*) as count
FROM jobs
GROUP BY job_title
ORDER BY count DESC
LIMIT 10;

-- Average salary by experience level
SELECT experience_level, AVG(salary_in_usd) as avg_salary
FROM jobs
GROUP BY experience_level
ORDER BY avg_salary DESC;

-- Remote work distribution
SELECT remote_ratio, COUNT(*) as count
FROM jobs
GROUP BY remote_ratio;

-- Top hiring locations
SELECT company_location, COUNT(*) as count
FROM jobs
GROUP BY company_location
ORDER BY count DESC
LIMIT 10;
```

### 3. Visualizations (saved in `/visuals`)
- Bar chart: Top job titles by frequency
- Bar chart: Average salary by experience level
- Pie chart: Remote vs hybrid vs on-site distribution
- Bar chart: Top company locations

---

## 📦 Requirements

```
pandas
matplotlib
```
> SQLite3 is part of Python's standard library — no extra install needed.

---

## 💡 What I Learned

- End-to-end data pipeline: raw CSV → cleaned data → SQL database → analysis → visualization
- Writing analytical SQL queries with `GROUP BY`, `ORDER BY`, `AVG()`, `COUNT()`
- Data cleaning techniques using Pandas (null handling, type conversion, deduplication)
- Structuring a multi-file Python project with separation of concerns
- Translating data insights into visual outputs for non-technical audiences

---

## 🔮 Future Improvements

- [ ] Integrate AWS S3 for cloud-based data storage
- [ ] Build an interactive dashboard using Streamlit
- [ ] Add salary prediction using a simple ML model
- [ ] Automate data refresh with a scheduled pipeline

---

## 👩‍💻 Author

**Afshan Chohan**
MSc Data Engineering & Information Management | AWS Cloud Practitioner

🔗 [LinkedIn](https://www.linkedin.com/in/afshan-chohan/) · [GitHub](https://github.com/afshan-chohan)

