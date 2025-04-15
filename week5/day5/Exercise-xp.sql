-- Exercise 1: DVD Rental

-- 1
SELECT * FROM language

-- 2
SELECT film.title, film.description, language.name FROM film JOIN language ON film.language_id = language.language_id;

-- 3
SELECT language.name, film.title, film.description FROM language LEFT JOIN film ON film.language_id = language.language_id;

-- 4
INSERT INTO new_film (name)
VALUES ('Anchorman'), ('Cinderella'), ('Mama Mia');
SELECT * FROM new_film;

-- 5
CREATE TABLE customer_review (
  review_id SERIAL NOT NULL PRIMARY KEY, 
  film_id INTEGER REFERENCES film(film_id) ON DELETE CASCADE,
  language_id INTEGER REFERENCES language(language_id),
  title TEXT,
  score SMALLINT,
  review_text TEXT,
  last_update DATE
);

-- 6
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update) 
VALUES 
(133,1,'Chamber Italian Review', 8, 'Movie was very good but emotional to watch', '2025-04-15'),
(384, 1, 'Grosse Wonderful Review', 2, 'Terrible movie', '2025-04-15');

SELECT * FROM new_film;

-- 7
-- Nothing will happen if I don't reference new_film id to customer_review

-- Exercise 2: DVD Rental
-- 1
UPDATE customer_review
SET language_id = 2  -- Italian
WHERE film_id IN (10, 20, 100);

-- 2
-- FK for customer table is customer_id. 

-- 3
-- Dropping customer_review table will be easy without FK constraints. Using DROP TABLE customer_review CASCADE should complete the job.

-- 4
SELECT COUNT(*) 
FROM rental
WHERE return_date IS NULL;

-- 5
SELECT * FROM film
WHERE rental_duration IS NULL
ORDER BY rental_rate DESC
LIMIT 30;

-- 6.1
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.description LIKE '%sumo wrestler%'  -- Looking for films whose description mentions "sumo wrestler"
AND a.first_name = 'Penelope'              
AND a.last_name = 'Monroe'; 

-- 6.2
SELECT f.title
FROM film f
WHERE f.length < 60  
AND f.rating = 'R';

-- 6.3
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew'
AND c.last_name = 'Mahan'
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01'
AND f.rental_rate > 4.00;

-- 6.4
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew'
AND c.last_name = 'Mahan'
AND (f.title LIKE '%boat%' OR f.description LIKE '%boat%')
AND f.replacement_cost > 20.00;