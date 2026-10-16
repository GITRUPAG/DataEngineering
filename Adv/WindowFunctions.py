import pandas as pd

data = {
    "product": ["Laptop", "phone", "Laptop", "phone", "Tablet"],
    "sales": [50000, 20000, 30000, 15000, 10000]
}

df = pd.DataFrame(data)

print(df)

df["running_total"] = df["sales"].cumsum()

print(df)

df["previous_sales"] = df["sales"].shift(1)
print(df)

df["rank"] = df["sales"].rank(ascending=False).astype(int)
print(df)