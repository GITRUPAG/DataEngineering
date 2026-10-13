import pandas as pd

df = pd.read_csv("sales.csv",
                 usecols=["order_id", "price"], nrows = 2)

print(df)

dfj = pd.read_json("student.json")

print(dfj)

#write to CSV

df.to_csv("output.csv",index=False)

dfj.to_json("output.json", orient="records")