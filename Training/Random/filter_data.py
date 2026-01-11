import pandas as pd

# Sample dataframe 
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 35, None, 42, 28],
    "Grade": ["A", "B", "C", "A", "B"]
}

df = pd.DataFrame(data)
#print(data)


# Filter rows with age > 30
filtered_df = df[df["Age"] > 30]
print("\nFiltered DataFrame (Age > 30): \n", filtered_df)

# Sort DataFrame by age in ascending order (default) 
sorted_df = df.sort_values("Age", ascending=False)   # Can assign an attribure to do "Decending"     sort_value("Age", ascending=False)  as ascending is default
print("\nSorted DataFrame by Age (ascending):\n", sorted_df)


# Check for missing values
print("\nMissing values in DataFrame:\n", df.isnull())

# Clean data by dropping rows where age is none
cleaned_df = df.dropna(subset=["Age"])

print("\nCleaned Data after none row removed from Age:\n", cleaned_df)

# Fill missing value 
filled_df = df.fillna({"Age": 30})
print("\nDataFrame after filling missing Age with 30:\n", filled_df)

# Remove Duplicate data 
# Add duplicate row for testing
df_with_dup = pd.concat([df, df.iloc[[1]]], ignore_index=True)
print("\nDuplicated added:\n", df_with_dup)

no_dup = df_with_dup.drop_duplicates()
print("\nDataFrame w/out dup:\n", no_dup)







