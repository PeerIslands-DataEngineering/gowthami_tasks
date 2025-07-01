-- ### Q1. Write a query to create a new column called `rating_category` with three categories based on the `ratings` column:
-- - **High** → ratings **greater than or equal to 4.30**    
-- - **Medium** → ratings **between 3.50 and 4.30 (exclusive of 4.30)**    
-- - **Low** → ratings **less than or equal to 3.50**  

-- Then, for each category, calculate:
-- 1. The total count of products    
-- 2. The total sales    
-- 3. The percentage contribution of each category to the overall count and overall sales.   

-- Exclude rows where the `ratings` column is NULL. Do **not** modify the original table.





SELECT * FROM bigbascketproducts.bigbasketproducts;
use bigbascketproducts;

with Categories as(
SELECT
 *,
 CASE
  WHEN rating >= 4.30 THEN 'high'
  WHEN rating BETWEEN 3.50 AND 4.30 THEN 'medium'
  ELSE 'low'
 END AS rating_category
FROM
 bb_products
where rating is not null

)
select 
 rating_category,
    COUNT(*) as total_count,
    SUM(sale_price) as total_sale_price,
    concat(round((COUNT(*) * 100.0) / (SELECT COUNT(*) FROM Categories), 2), ' %') AS count_percentage,
    concat(round((SUM(sale_price) * 100.0) / (SELECT SUM(sale_price) FROM Categories),2), ' %') as sale_price_percentage

from categories
GROUP BY rating_category;