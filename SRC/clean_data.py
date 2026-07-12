import pandas as pd

# Read datasets
customers = pd.read_csv("../DATA/RAW/customers.csv")
orders = pd.read_csv("../DATA/RAW/orders.csv")
order_items = pd.read_csv("../DATA/RAW/order_items.csv")
products = pd.read_csv("../DATA/RAW/products.csv")

# Remove duplicate customers
customers.drop_duplicates(inplace=True)

# Fill missing customer names
customers["customer_name"] = customers["customer_name"].fillna("Unknown")

# Standardize city names
customers["city"] = customers["city"].str.strip().str.title()

# Remove negative quantity
order_items = order_items[order_items["quantity"] > 0]

# Fill missing price
order_items["price"] = order_items["price"].fillna(order_items["price"].mean())



# Save cleaned data
customers.to_csv("../DATA/CLEAN/clean_customers.csv", index=False)
orders.to_csv("../DATA/CLEAN/clean_orders.csv", index=False)
order_items.to_csv("../DATA/CLEAN/clean_order_items.csv", index=False)
products.to_csv("../DATA/CLEAN/clean_products.csv", index=False)
print("Data cleaned successfully!")


# Remove duplicate rows
products = products.drop_duplicates()

# Save cleaned products
products.to_csv("../DATA/CLEAN/clean_products.csv", index=False)

print("Products cleaned successfully!")
