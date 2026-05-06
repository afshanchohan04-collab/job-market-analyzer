import pandas as pd

# Load dataset
df = pd.read_csv('../data/jobs.csv')

df = df.drop(columns=['unnamed:_0'], errors='ignore')

print(df.columns)

# Show first rows
print("First 5 rows:\n", df.head())

# Show columns
print("\nColumns:\n", df.columns)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Drop duplicates
df = df.drop_duplicates()

# Check missing values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing values (simple approach)
df = df.fillna('Not Specified')

# Save cleaned file
df.to_csv('../data/cleaned_jobs.csv', index=False)

print("\n✅ Cleaned data saved!")
