CREATE DATABASE ecommerce_analytics;
USE ecommerce_analytics;
SHOW TABLES;
CREATE TABLE customers(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
signup_date DATE
);
CREATE TABLE products(
product_id VARCHAR(10) PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);
CREATE TABLE orders(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
status VARCHAR(20),
FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
CREATE TABLE order_items(
order_item_id INT PRIMARY KEY,
order_id INT,
product_id VARCHAR(10),
quantity INT,
price DECIMAL(10,2),
FOREIGN KEY(order_id) REFERENCES orders(order_id),
FOREIGN KEY(product_id) REFERENCES products(product_id)
);
show tables;

SELECT COUNT(*) AS Customers FROM customers;
SELECT COUNT(*) AS Products FROM products;
SELECT COUNT(*) AS Orders FROM orders;
SELECT COUNT(*) AS Order_Items FROM order_items;

SELECT SUM(quantity * price) AS Total_Revenue
FROM order_items;
SELECT
    c.customer_id,
    c.customer_name,
    SUM(oi.quantity * oi.price) AS Revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.customer_name
ORDER BY Revenue DESC
LIMIT 10;
SELECT
    p.product_name,
    SUM(oi.quantity) AS Total_Sold
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY Total_Sold DESC;

SELECT
    DATE_FORMAT(o.order_date,'%Y-%m') AS Month,
    SUM(oi.quantity * oi.price) AS Revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY Month
ORDER BY Month;

SELECT
    c.customer_name,
    COUNT(o.order_id) AS Total_Orders,
    SUM(oi.quantity * oi.price) AS Revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.customer_name;

SELECT
    p.category,
    SUM(oi.quantity * oi.price) AS Revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY Revenue DESC;

SELECT
AVG(Order_Total) AS Avg_Order_Value
FROM (
SELECT
order_id,
SUM(quantity * price) AS Order_Total
FROM order_items
GROUP BY order_id
) t;

SELECT
    c.city,
    SUM(oi.quantity * oi.price) AS Revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.city
ORDER BY Revenue DESC
LIMIT 5;
 
 
 
 
 
 SELECT
p.category,
SUM(oi.quantity*oi.price) AS Revenue

FROM order_items oi
JOIN products p
ON oi.product_id=p.product_id

GROUP BY p.category
ORDER BY Revenue DESC;




SELECT

DATE_FORMAT(o.order_date,'%Y-%m') Month,

SUM(oi.quantity*oi.price) Revenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY Month;

WITH MonthlyRevenue AS
(
SELECT
DATE_FORMAT(o.order_date,'%Y-%m') AS Month,
SUM(oi.quantity*oi.price) AS Revenue

FROM orders o

JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY DATE_FORMAT(o.order_date,'%Y-%m')
)

SELECT *
FROM MonthlyRevenue;



SELECT

customer_id,

SUM(quantity*price) Revenue,

RANK() OVER(
ORDER BY SUM(quantity*price) DESC
) CustomerRank

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY customer_id;






SELECT

product_name,

price,

ROW_NUMBER()

OVER(

ORDER BY price DESC

) AS RowNumber

FROM products;




SELECT

DATE_FORMAT(order_date,'%Y-%m') Month,

SUM(quantity*price) Revenue,

SUM(SUM(quantity*price))

OVER(

ORDER BY DATE_FORMAT(order_date,'%Y-%m')

) RunningRevenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY Month;





SELECT

customer_id,

CASE

WHEN COUNT(order_id)>=10

THEN 'High Value'

WHEN COUNT(order_id)>=5

THEN 'Medium Value'

ELSE 'Low Value'

END CustomerSegment

FROM orders

GROUP BY customer_id;


SELECT
DATE_FORMAT(signup_date,'%Y-%m') AS Cohort_Month,
COUNT(customer_id) AS New_Customers
FROM customers
GROUP BY DATE_FORMAT(signup_date,'%Y-%m')
ORDER BY Cohort_Month;
    
    
    
    
    
    SELECT
p.product_name,
SUM(oi.quantity) AS Quantity_Sold,
SUM(oi.quantity * oi.price) AS Revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY Revenue DESC
LIMIT 5;


