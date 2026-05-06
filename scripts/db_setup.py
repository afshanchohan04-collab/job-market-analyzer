import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv('../data/cleaned_jobs.csv')

# Create database
conn = sqlite3.connect('../data/jobs.db')

# Save to SQL table
df.to_sql('jobs', conn, if_exists='replace', index=False)

print("✅ Data inserted into database!")

# Run sample query
query = """
SELECT job_title, AVG(salary_in_usd) as avg_salary
FROM jobs
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 10;
"""

result = pd.read_sql(query, conn)

print("\nTop Paying Job Titles:\n", result)

conn.close()
