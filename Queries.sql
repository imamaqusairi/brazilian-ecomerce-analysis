-- Current Situation (Jan - Oct 2018): 
-- 1. Total Order -- Done
-- 2. Total Gross Merchandising Value (GMV) -- Done
-- 3. Total Net Revenue -- Done
-- 4. Average Order Value (AOV) -- Done
-- 5. Retention Rate (1 Year)
-- 6. 3 Top City Contributor (Based on GMV)
-- 7. 3 Top States Contributor (Based on GMV)
-- 8. 5 Most Favored Product 

-- Total Order
-- SELECT 
-- 	COUNT 
-- 		(DISTINCT order_id) AS total_order
-- FROM
-- 	public."order"
-- WHERE
-- 	order_purchase_timestamp BETWEEN '2018-01-01 00:00:00' AND '2018-12-31 23:59:59'
	
-- ADDITIONAL : ADJUST DATA FORMAT 
-- ALTER TABLE public.order 
-- ALTER COLUMN order_purchase_timestamp TYPE TIMESTAMP 
-- USING order_purchase_timestamp::TIMESTAMP;

-- Total Gross Merchandising Value (GMV)
-- SELECT 
-- 	SUM(table1."price") AS GMV 
-- FROM 
-- 	public."order item" table1
-- INNER JOIN 
-- 	public."order" table2
-- ON
-- 	table1."order_id" = table2."order_id"
-- WHERE 	
-- 	table2."order_purchase_timestamp" BETWEEN '2018-01-01 00:00:00' AND '2018-12-31 23:59:59'


-- Total Net Revenue (Total Price - Total Freight)
-- SELECT 
-- 	(SUM(table1.price) - SUM(table1.freight_value)) "Net REVENUE"
-- FROM
-- 	public."order item" table1
-- INNER JOIN
-- 	public."order" table2
-- ON 
-- 	table1."order_id" = table2."order_id"
-- WHERE
-- 	table2."order_purchase_timestamp" BETWEEN '2018-01-01 00:00:00' AND '2018-12-31 23:59:59'


-- Average Order Value (AOV)
-- SELECT 
-- 	(SUM(table1.price) / COUNT(table1."order_id")) "Average Order Value"
-- FROM 
-- 	public."order item" table1
-- INNER JOIN
-- 	public."order" table2
-- ON
-- 	table1."order_id" = table2."order_id"
-- WHERE
-- 	table2."order_purchase_timestamp" BETWEEN '2018-01-01 00:00:00' AND '2018-12-31 23:59:59'
