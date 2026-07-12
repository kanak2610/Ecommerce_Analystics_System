import pandas as pd

# Load cleaned data
customers = pd.read_csv("../DATA/CLEAN/clean_customers.csv")
orders = pd.read_csv("../DATA/CLEAN/clean_orders.csv")
order_items = pd.read_csv("../DATA/CLEAN/clean_order_items.csv")
products = pd.read_csv("../DATA/RAW/products.csv")

print("="*50)
print("DATA VALIDATION STARTED")
print("="*50)

# -------------------------------
# Duplicate Checks
# -------------------------------

if customers["customer_id"].duplicated().sum() == 0:
    print("✓ No Duplicate Customer IDs")
else:
    print("✗ Duplicate Customer IDs Found")

if orders["order_id"].duplicated().sum() == 0:
    print("✓ No Duplicate Order IDs")
else:
    print("✗ Duplicate Order IDs Found")

if products["product_id"].duplicated().sum() == 0:
    print("✓ No Duplicate Product IDs")
else:
    print("✗ Duplicate Product IDs Found")

# -------------------------------
# Missing Values
# -------------------------------

print("\nMissing Values:")

print(customers.isnull().sum())
print(orders.isnull().sum())
print(order_items.isnull().sum())

# -------------------------------
# Negative Quantity
# -------------------------------

if "quantity" in order_items.columns:
    if (order_items["quantity"] < 0).sum() == 0:
        print("\n✓ No Negative Quantity")
    else:
        print("\n✗ Negative Quantity Found")

# -------------------------------
# Negative Price
# -------------------------------

if "price" in products.columns:
    if (products["price"] < 0).sum() == 0:
        print("✓ No Negative Price")
    else:
        print("✗ Negative Price Found")

# -------------------------------
# Foreign Key Validation
# -------------------------------

invalid_customer = orders[
    ~orders["customer_id"].isin(customers["customer_id"])
]

if len(invalid_customer) == 0:
    print("✓ Customer Foreign Key Valid")
else:
    print("✗ Invalid Customer IDs Found")

# Convert to same datatype
orders["order_id"] = orders["order_id"].astype(str).str.strip()
order_items["order_id"] = order_items["order_id"].astype(str).str.strip()

invalid_order = order_items[
    ~order_items["order_id"].isin(orders["order_id"])
]

if len(invalid_order) == 0:
    print("✓ Order Foreign Key Valid")
else:
    print("✗ Invalid Order IDs Found")
    print(invalid_order)
print("\n")
print("="*50)
print("VALIDATION COMPLETED")
print("="*50)