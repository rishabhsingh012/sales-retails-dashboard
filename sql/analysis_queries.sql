-- Revenue by category
SELECT Category, SUM(Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

-- Top 10 customers by revenue
SELECT Customer_Name, SUM(Sales) as total_sales
FROM sales
GROUP BY Customer_Name
ORDER BY total_sales DESC
LIMIT 10;

-- Sales by region
SELECT Region, SUM(Sales) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;

-- Monthly sales trend
SELECT substr(Order_Date, 1, 7) AS order_month, SUM(Sales) AS total_sales
FROM sales
GROUP BY order_month
ORDER BY order_month;

-- Sales by ship mode
SELECT Ship_Mode, SUM(Sales) AS total_sales
FROM sales
GROUP BY Ship_Mode
ORDER BY total_sales DESC;

