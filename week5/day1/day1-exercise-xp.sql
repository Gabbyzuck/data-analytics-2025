CREATE TABLE public.items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    price INTEGER NOT NULL
);

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

INSERT INTO items (item_name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

INSERT INTO customers (first_name, last_name, email) VALUES
('Greg', 'Jones', 'gjones@gmail.com'),
('Sandra', 'Jones', 'sjones@gmail.com'),
('Scott', 'Scott', 'sscott@gmail.com'),
('Trevor', 'Green', 'tgreen@gmail.com'),
('Melanie', 'Johnson', 'mjohnson@gmail.com');

-- 1. All the items.
SELECT * FROM items;

-- 2. All the items with a price above 80 (80 not included).
SELECT * FROM items WHERE price > 80;

-- 3. All the items with a price below 300. (300 included)
SELECT * FROM items WHERE price <= 300;

-- 4. All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customers WHERE last_name = 'Smith';

-- 5. All customers whose last name is ‘Jones’.
SELECT * FROM customers WHERE last_name is 'Jones';

-- 6. All customers whose firstname is not ‘Scott’.
SELECT * FROM customers WHERE first_name != 'Scott';
