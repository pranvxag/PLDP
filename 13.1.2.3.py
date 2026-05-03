import pandas as pd

# Create first DataFrame
data1 = {
    "Name": ["Pranav", "Rahul", "Amit"],
    "Age": [20, 21, 22]
}

df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    "Name": ["Sneha", "Pooja"],
    "Age": [23, 24]
}

df2 = pd.DataFrame(data2)

# Task 1: Display last N rows using tail()
N = 2
print("Last", N, "rows:")
print(df1.tail(N))

# Task 2: Add a new column
df1["City"] = ["Pune", "Mumbai", "Nashik"]
print("\nDataFrame after adding new column:")
print(df1)

# Task 3: Concatenate two DataFrames
result = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame:")
print(result)
