import pandas as pd              # Import the pandas library to work with data in Python.

# Read the CSV file into a DataFrame
df = pd.read_csv("data/sample/sample_events.csv")

# Print the shape of the DataFrame, the list of columns, and the first few rows
print(df.shape)
print(list(df.columns))
print(df.head())

# Count how many different events there are
print(df["event_id"].nunique())

# Count how many reports each event has
print(df["event_id"].value_counts())