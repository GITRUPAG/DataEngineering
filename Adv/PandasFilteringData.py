import pandas as pd

data = [
    {"name": "ravi", "age": 22},
{"name": "arun", "age": 20},
{"name": "rahul", "age": 18000},
{"name": "priya", "age": 35},
{"name": "priya", "age": 35},
{"name": "priya", "age": 40},
{"name": "priya"}
]

df = pd.DataFrame(data)

print(df)

high_marks = df[df["age"] > 25]  # [False, False, False, True

print(high_marks)

result = df[
    (df["age"] < 23) | (df["name"] == "arun")
]

print(result)

print("ISIN")

values = df[df["name"].isin(["ravi", "arun", "alice"])]

print(values)

print("Filtering missing values")

res = df[df["age"].notna()]

print(res)