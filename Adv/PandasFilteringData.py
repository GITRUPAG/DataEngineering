import pandas as pd

data = [
    {"name": "ravi", "age": 22},
{"name": "arun", "age": 20},
{"name": "rahul", "age": 18000},
{"name": "priya", "age": 35},
{"name": "bob", "age": 35},
{"name": "alice", "age": 40},
{"name": "priya New"}
]



df = pd.DataFrame(data)


print(df)

high_marks = df[df["age"] > 25]  # [False, False, False, True

print(high_marks)

result = df[
    (df["age"] < 23) | (df["name"] == "arun")
]

# &, |, ~

print(result)

print("ISIN")

values = df[df["name"].isin(["ravi", "arun", "alice"])]

print(values)

print("Filtering missing values")

res = df[df["age"].notna()]

print(res)


df["passed"] = [True, True, False, True, True,False, True]

print(df)

sales = pd.DataFrame({
    "quantity":[2,None,5],
    "price":[100,None, None]
})

sales["total"] = sales["quantity"] * sales["price"]

print(sales)

sales = sales.rename(columns={"total": "total_value"})

print(sales)

# sales = sales.drop(columns=["total_value"])

#handling missing values
print("Missing values")
print(sales.isna()) # identifies missing values

print(sales.isna().sum()) # count missing values

# print(sales.dropna())

print(sales.fillna(0))
data = {
    "name":["R", None, "B", "R", "Rupa"],
    "age":[22,None,20,22,22]
}

data1 = pd.DataFrame(data)

print(data1)

data1["age"] = data1["age"].fillna(0)

print(data1)

# Removing duplicates

data1 = data1.drop_duplicates(subset="age", keep="last")
print(data1)


print(data1.dtypes)

data2 = {
    "name":["R", None, "B", "R", "Rupa"],
    "age":["22",10,"20","22","22"]
}

df = pd.DataFrame(data2)

print(df.dtypes)

df["age"] = df["age"].astype(int) # change the data type int, float, str, bool

print(df.dtypes)


# df["marks"] = pd.to_numeric(
#     df["marks"], errors = "coerce"
# )  # Converts to NaN

# Sorting data sort_values

result = df.sort_values(by="age", ascending=False)

#result = df.sort_values(by=["age","marks"], ascending=[True, False])

print(result)




