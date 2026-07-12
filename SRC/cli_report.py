import mysql.connector
import pandas as pd
import sys


# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Avnik@2235",
    database="ecommerce_analytics"
)

report = sys.argv[1].lower()

if report == "customer":

    query = """
    SELECT
        c.customer_name,
        COUNT(o.order_id) AS Total_Orders,
        SUM(oi.quantity * oi.price) AS Revenue
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    JOIN order_items oi
    ON o.order_id = oi.order_id
    GROUP BY c.customer_name
    ORDER BY Revenue DESC;
    """

    df = pd.read_sql(query, conn)
    print(df.head(10))
    df.to_csv("../REPORTS/customer_report.csv", index=False)
    print("\nCustomer Report Generated Successfully!")

elif report == "revenue":

    query = """
    SELECT
        DATE_FORMAT(order_date,'%Y-%m') AS Month,
        SUM(quantity*price) AS Revenue
    FROM orders o
    JOIN order_items oi
    ON o.order_id=oi.order_id
    GROUP BY Month
    ORDER BY Month;
    """

    df = pd.read_sql(query, conn)
    print(df)
    df.to_csv("../REPORTS/revenue_report.csv", index=False)
    print("\nRevenue Report Generated Successfully!")

elif report == "retention":

    query = """
    SELECT
        customer_id,
        COUNT(order_id) AS Total_Orders
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(order_id)>1;
    """

    df = pd.read_sql(query, conn)
    print(df)
    df.to_csv("../REPORTS/retention_report.csv", index=False)
    print("\nRetention Report Generated Successfully!")

else:
    print("Invalid Report!")
    print("Use:")
    print("python cli_report.py customer")
    print("python cli_report.py revenue")
    print("python cli_report.py retention")

conn.close()