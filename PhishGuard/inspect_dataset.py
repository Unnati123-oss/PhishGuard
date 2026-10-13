import pandas as pd
from pathlib import Path

# Locate the dataset
file_path = Path("data/PhiUSIIL_Phishing_URL_Dataset.csv")

# Check whether the file exists
if not file_path.exists():
    print("Dataset not found!")
    print("Files available in data folder:")
    for file in Path("data").glob("*"):
        print(file.name)
    raise SystemExit

# Load the dataset
df = pd.read_csv(file_path, low_memory=False)

# 1. Dataset dimensions
print("\n--- DATASET SIZE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Column names
print("\n--- COLUMN NAMES ---")
for column in df.columns:
    print(column)

# 3. First five rows
print("\n--- FIRST FIVE ROWS ---")
print(df.head().to_string())

# 4. Data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 5. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum().sort_values(ascending=False).head(15))

# 6. Duplicate rows
print("\n--- DUPLICATES ---")
print("Duplicate rows:", df.duplicated().sum())

# 7. Possible label columns
print("\n--- POSSIBLE LABEL COLUMNS ---")
for column in df.columns:
    if any(word in column.lower()
           for word in ["label", "class", "status", "result"]):
        print(f"\n{column}")
        print(df[column].value_counts(dropna=False))

print("\nInspection completed.")