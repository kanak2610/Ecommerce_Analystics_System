import pandas as pd
import argparse

# Command Line Arguments
parser = argparse.ArgumentParser(description="E-Commerce Reporting Tool")

parser.add_argument(
    "--report",
    choices=["sales", "customers", "products"],
    required=True,
    help="Choose report type"
)

args = parser.parse_args()

# Load Data
orders = pd.read_csv("../DATA/CLEAN/clean_orders.csv")
customers = pd.read_csv("../DATA/CLEAN/clean_customers.csv")
products = pd.read_csv("../DATA/CLEAN/clean_products.csv")
order_items = pd.read_csv("../DATA/CLEAN/clean_order_items.csv")

# Calculate Revenue
order_items["Revenue"] = order_items["quantity"] * order_items["price"]

# Reports
if args.report == "sales":

    print("\n========== SALES REPORT ==========")
    print("Total Orders    :", orders["order_id"].nunique())
    print("Total Revenue   : ₹", round(order_items["Revenue"].sum(), 2))

elif args.report == "customers":

    print("\n========== CUSTOMER REPORT ==========")
    print("Total Customers :", customers["customer_id"].nunique())

elif args.report == "products":

    print("\n========== PRODUCT REPORT ==========")
    print("Total Products  :", products["product_id"].nunique())