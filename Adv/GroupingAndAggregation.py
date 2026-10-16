import pandas as pd

data = {
    "product":["Laptop", "phone","Laptop", "phone","Tablet"],
    "sales":[50000,20000,30000,15000,10000]
}

df = pd.DataFrame(data)

print(df)

result = df.groupby("product")
print(result.groups)


total = df.groupby("product")["sales"].sum()
print(total)
#total = df.groupby(["product", "city"])["sales"].sum()

# mean(), count(), min(), ,max(), median()

res = df.groupby("product").agg(
    total_sales =("sales", "sum"),
    average_sales = ("sales","mean"),
    highest_sales = ("sales", "max")
)

print(res)




