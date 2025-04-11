-- Exercise 2: dvdrental database
-- 1
SELECT * FROM customer;

-- 2
SELECT first_name, last_name FROM customer AS full_name;

-- 3
SELECT DISTINCT create_date FROM customer;

-- 4
SELECT * FROM customer ORDER BY first_name DESC;

-- 5
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

-- 6
SELECT address, phone FROM address WHERE district = 'Texas';

-- 7
SELECT * FROM film WHERE film_id = 15 OR film_id = 150;

-- 8 
SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Back To The Future';

-- 9
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Ba%';

-- 10
SELECT title, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;

-- 11
WITH film AS (SELECT title, rental_rate,
ROW_NUMBER() OVER (ORDER BY rental_rate ASC)
AS row_num FROM film
)
SELECT title, rental_rate FROM film WHERE row_num BETWEEN 11 AND 20;

-- 12
SELECT first_name, last_name, amount, payment_date FROM customer JOIN payment ON customer.customer_id = payment.customer_id ORDER BY customer.customer_id ASC;

-- 13
 SELECT * FROM film LEFT OUTER JOIN inventory ON film.film_id = inventory.film_id;

 -- 14
 SELECT * FROM city INNER JOIN country ON city.country_id = country.country_id;

 -- 15
 SELECT staff_id,payment.customer_id, first_name, last_name, amount, payment_date FROM payment 
 JOIN customer ON payment.customer_id = customer.customer_id
 ORDER BY staff_id;