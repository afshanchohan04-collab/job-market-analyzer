import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('../data/cleaned_jobs.csv')

# -------------------------------
# 1. Most Common Job Titles
# -------------------------------
top_jobs = df['job_title'].value_counts().head(10)

print("\nTop Job Titles:\n", top_jobs)

# Plot
top_jobs.plot(kind='bar')
plt.title("Top 10 Job Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../visuals/top_job_titles.png')
plt.clf()


# -------------------------------
# 2. Average Salary by Experience
# -------------------------------
salary_exp = df.groupby('experience_level')['salary_in_usd'].mean()

print("\nAverage Salary by Experience:\n", salary_exp)

salary_exp.plot(kind='bar')
plt.title("Average Salary by Experience Level")
plt.tight_layout()
plt.savefig('../visuals/salary_by_experience.png')
plt.clf()


# -------------------------------
# 3. Remote Work Distribution
# -------------------------------
remote = df['remote_ratio'].value_counts()

print("\nRemote Work Distribution:\n", remote)

remote.plot(kind='pie', autopct='%1.1f%%')
plt.title("Remote Work Ratio")
plt.ylabel('')
plt.savefig('../visuals/remote_ratio.png')
plt.clf()


# -------------------------------
# 4. Top Company Locations
# -------------------------------
locations = df['company_location'].value_counts().head(10)

print("\nTop Company Locations:\n", locations)

locations.plot(kind='bar')
plt.title("Top Company Locations")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../visuals/top_locations.png')
plt.clf()

print("\n✅ Analysis completed and charts saved!")
