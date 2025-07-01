CREATE SCHEMA rev_diner;

use rev_diner;

CREATE TABLE sales (
  customer_id VARCHAR(50),
  order_date DATE,
  product_id INTEGER
);

INSERT INTO sales
  (customer_id, order_date, product_id)
VALUES
  ('Chinku', '2024-01-01', '1'),
  ('Chinku', '2024-01-01', '2'),
  ('Chinku', '2024-01-07', '2'),
  ('Chinku', '2024-01-10', '3'),
  ('Chinku', '2024-01-11', '3'),
  ('Chinku', '2024-01-11', '3'),
  ('Minku', '2024-01-01', '2'),
  ('Minku', '2024-01-02', '2'),
  ('Minku', '2024-01-04', '1'),
  ('Minku', '2024-01-11', '1'),
  ('Minku', '2024-01-16', '3'),
  ('Minku', '2024-02-01', '3'),
  ('Pinku', '2024-01-01', '3'),
  ('Pinku', '2024-01-01', '3'),
  ('Pinku', '2024-01-07', '3');
 
 
CREATE TABLE menu (
  product_id INTEGER,
  product_name VARCHAR(50),
  price INTEGER
);

INSERT INTO menu
  (product_id, product_name, price)
VALUES
  ('1', 'sushi', '10'),
  ('2', 'Paneer curry', '15'),
  ('3', 'Noodles', '12');
  

CREATE TABLE members (
  customer_id VARCHAR(50),
  join_date DATE
);

INSERT INTO members
  (customer_id, join_date)
VALUES
  ('Chinku', '2024-01-07'),
  ('Minku', '2024-01-09');
  
  
  
  
-- What was the first item from the menu purchased by each customer?
-- What is the most purchased item on the menu and how many times was it purchased by all customers?
-- Which item was the most popular for each customer?
-- Which item was purchased first by the customer after they became a member?
-- What is the total items and amount spent for each member before they became a member?
--  

SELECT s.customer_id, m.product_name
FROM sales s
JOIN menu m ON s.product_id = m.product_id
WHERE (s.customer_id, s.order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM sales
    GROUP BY customer_id
);



SELECT m.product_name, COUNT(*) AS total_orders
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY total_orders DESC
LIMIT 1;


WITH ranked_orders AS (
  SELECT
    s.customer_id,
    m.product_name,
    COUNT(*) AS order_count,
    RANK() OVER (PARTITION BY s.customer_id ORDER BY COUNT(*) DESC) AS rnk
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
  GROUP BY s.customer_id, m.product_name
)
SELECT customer_id, product_name, order_count
FROM ranked_orders
WHERE rnk = 1;


SELECT s.customer_id, m.product_name, s.order_date
FROM sales s
JOIN members mem ON s.customer_id = mem.customer_id
JOIN menu m ON s.product_id = m.product_id
WHERE s.order_date >= mem.join_date
AND (s.customer_id, s.order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM sales
    JOIN members ON sales.customer_id = members.customer_id
    WHERE sales.order_date >= members.join_date
    GROUP BY customer_id
);


SELECT 
  s.customer_id,
  COUNT(*) AS total_items,
  SUM(m.price) AS total_spent
FROM sales s
JOIN members mem ON s.customer_id = mem.customer_id
JOIN menu m ON s.product_id = m.product_id
WHERE s.order_date < mem.join_date
GROUP BY s.customer_id;
