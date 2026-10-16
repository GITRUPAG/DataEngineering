import pandas as pd

customers = pd.DataFrame({
    "customer_id":[1 , 2, 3, 4],
    "name":["Ravi", "Priya", "Amit", "Sneha"]
})

print(customers)


orders = pd.DataFrame({
    "customer_id":[1, 2, 2, 5],
    "product":["Laptop", "Phone", "Mouse", "Tablet"]
})

print(orders)

result = pd.merge(
    customers, orders,
    on="customer_id",
    how="inner"
)

print(result)

result = pd.merge(
    customers, orders,
    on="customer_id",
    how="left"
)

result = pd.merge(
    customers, orders,
    on="customer_id",
    how="right"
)

result_outer = pd.merge(
    customers, orders,
    on="customer_id",  #["customer_id, "region"]
    how="outer",
    suffixes =("_customer", "_order")
)

print(result_outer)


res = pd.merge(
    customers,
    orders.rename(columns={"customer_id": "order_id"}),
    left_on="customer_id",
    right_on="order_id",
    how="inner",
    validate="one_to_many"
)

print(res)


