import mysql.connector
import pandas as pd

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Avnik@2235",
    database="ecommerce_analytics"
)

cursor = conn.cursor()

print("Connected to Database Successfully!\n")

# Revenue Report
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

print(df)

# Save Report
df.to_csv("../REPORTS/customer_report.csv", index=False)

print("\nReport Saved Successfully!")



# Monthly Revenue Trend
query = """
SELECT
DATE_FORMAT(o.order_date,'%Y-%m') AS Month,
SUM(oi.quantity*oi.price) AS Revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY Month
ORDER BY Month;
"""

df = pd.read_sql(query, conn)

print("\nMonthly Revenue Report")
print(df)

df.to_csv("../REPORTS/revenue_report.csv", index=False)



query = """
SELECT
customer_id,

CASE

WHEN COUNT(order_id)>=10 THEN 'High Value'

WHEN COUNT(order_id)>=5 THEN 'Medium Value'

ELSE 'Low Value'

END AS Segment

FROM orders

GROUP BY customer_id;
"""

df = pd.read_sql(query, conn)

print("\nCustomer Segmentation")
print(df)

df.to_csv("../REPORTS/_report.csv", index=False)



query = """
SELECT
customer_id,
COUNT(order_id) AS TotalOrders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id)>1;
"""

df = pd.read_sql(query, conn)

print("\nRetention Report")
print(df)

df.to_csv("../REPORTS/retention_report.csv", index=False)

conn.close()