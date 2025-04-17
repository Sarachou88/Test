# Import packages
import pandas as pd

# Define the data
data = {
    "name": ["Alice", "Bob", None, "David"],
    "age": [25, None, 22, 29],
    "city": ["NYC", "LA", "Chicago", "Seattle"]
}

# Transform the data into a panda dataframe 
df = pd.DataFrame(data)

# Drop rows with missing names
cleaned_df = df.dropna(subset=["name"])

# Fill missing ages with average age
cleaned_df["age"] = cleaned_df["age"].fillna(cleaned_df["age"].mean())

# Show the dataset result
print(cleaned_df)
