import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Arun"],
    "age": [20,21,19]
}
df = pd.DataFrame(data,
                  index = ["S101", "S102", "S103"]) # converts dictionary into table

print(df.loc["S101", "name"])
print(df)

print(df["name"]) # return a series

# 2
# Series and DataFrames
marks = pd.Series([20, 52, 30],
                  index = ["ravi", "Priya", "arun"]) # 1D labeleed array

print(marks)
print(marks["ravi"])

data = [
    {"name":"ravi", "age":22},
{"name":"arun", "age":20},
{"name":"rahul", "age":18},
{"name":"priya", "age":35},
{"name":"priya", "age":35},
{"name":"priya", "age":35},
{"name":"priya", "age":35}
]

df1 = pd.DataFrame(data)

print(df1)

print(df1.head(2)) # first five rows

print(df1.tail()) # last five rows

print(df1.info())

print(df1.shape) # Number of rows and columns

print(df1.columns) # column names

print(df1.dtypes) # data types of each column

print(df1.index) # Row Index




