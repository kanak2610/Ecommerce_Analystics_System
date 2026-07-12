import pandas as pd
from faker import Faker
import random

fake = Faker("en_IN")

# -----------------------------
# Generate Customers
# -----------------------------

customers = []

for i in range(1, 1001):
    customers.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "city": fake.city(),
        "signup_date": fake.date_between(start_date="-3y", end_date="today")
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# Generate Products
# -----------------------------

products = [
    ["P001", "Laptop", "Electronics", 55000],
    ["P002", "Mobile", "Electronics", 25000],
    ["P003", "Headphones", "Electronics", 2000],
    ["P004", "Shoes", "Fashion", 3000],
    ["P005", "T-Shirt", "Fashion", 800],
    ["P006", "Watch", "Accessories", 5000],
    ["P007", "Book", "Books", 500],
    ["P008", "Keyboard", "Electronics", 1200],
    ["P009", "Mouse", "Electronics", 700],
    ["P010", "Bag", "Accessories", 1500]
]

products_df = pd.DataFrame(
    products,
    columns=["product_id", "product_name", "category", "price"]
)

# -----------------------------
# Generate Orders
# -----------------------------

status = ["Delivered", "Cancelled", "Returned", "Pending"]

orders = []

for i in range(1, 5001):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 1000),
        "order_date": fake.date_between(start_date="-2y", end_date="today"),
        "status": random.choice(status)
    })

orders_df = pd.DataFrame(orders)

# -----------------------------
# Generate Order Items
# -----------------------------

order_items = []

prices = [55000, 25000, 2000, 3000, 800, 5000, 500, 1200, 700, 1500]

for i in range(1, 10001):
    order_items.append({
        "order_item_id": i,
        "order_id": random.randint(1, 5000),
        "product_id": f"P{random.randint(1,10):03}",
        "quantity": random.randint(1,5),
        "price": random.choice(prices)
    })

order_items_df = pd.DataFrame(order_items)

# -----------------------------
# Add Dirty Data
# -----------------------------

# Missing customer name
customers_df.loc[5, "customer_name"] = None

# Duplicate customer
customers_df = pd.concat(
    [customers_df, customers_df.iloc[[10]]],
    ignore_index=True
)

# Wrong city names
customers_df.loc[15, "city"] = "JAIPUR"
customers_df.loc[16, "city"] = "jaipur"
customers_df.loc[17, "city"] = " Jaipur "

# Negative quantity
order_items_df.loc[20, "quantity"] = -3

# Missing price
order_items_df.loc[25, "price"] = None

# Future order date
orders_df.loc[30, "order_date"] = "2035-01-01"

# -----------------------------
# Save RAW Files
# -----------------------------

customers_df.to_csv("../DATA/RAW/customers.csv", index=False)
products_df.to_csv("../DATA/RAW/products.csv", index=False)
orders_df.to_csv("../DATA/RAW/orders.csv", index=False)
order_items_df.to_csv("../DATA/RAW/order_items.csv", index=False)

print("customers.csv created successfully!")
print("products.csv created successfully!")
print("orders.csv created successfully!")
print("order_items.csv created successfully!")
print("Dirty data added successfully!")