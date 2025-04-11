-- Exercise 1: Items and Customers
-- 1
SELECT * FROM items ORDER BY price ASC;

-- 2
SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

-- 3
SELECT first_name, last_name FROM customers 
ORDER BY first_name ASC 
LIMIT 3;

-- 4
SELECT last_name FROM customers
ORDER BY last_name DESC;



