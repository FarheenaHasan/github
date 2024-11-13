import pandas as pd

# Load the dataset
df = pd.read_csv('chess_dataset.csv')

# Display the first few rows of the dataset
print("Initial dataset:")
print(df.head())

# Drop rows with missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert categorical columns to numerical values (if any)
# Example: Convert 'Result' column to numerical values
df['Result'] = df['Result'].map({'win': 1, 'loss': 0, 'draw': 0.5})

# Normalize/Standardize numerical columns (if necessary)
# Example: Normalize 'Rating' column
df['Rating'] = (df['Rating'] - df['Rating'].mean()) / df['Rating'].std()

# Display the cleaned dataset
print("Cleaned dataset:")
print(df.head())

# Save the cleaned dataset to a new CSV file
df.to_csv('cleaned_chess_dataset.csv', index=False)