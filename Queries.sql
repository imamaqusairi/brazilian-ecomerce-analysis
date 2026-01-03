-- Current Situation (Jan - Oct 2018): 
-- 1. Total Order
-- 2. Total Gross Merchandising Value (GMV)
-- 3. Total Net Revenue 
-- 4. Average Order Value (AOV)
-- 5. Retention Rate (1 Year)
-- 6. 3 Top City Contributor (Based on GMV)
-- 7. 3 Top States Contributor (Based on GMV)
-- 8. 5 Most Favored Product 

-- -- Total Order
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
