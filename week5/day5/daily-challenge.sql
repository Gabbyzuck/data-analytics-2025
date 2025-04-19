-- Part I
-- 1
CREATE TABLE customer (
	id SERIAL PRIMARY KEY, 
	first_name text NOT NULL,
	last_name text NOT NULL
) 

CREATE TABLE customer_profile (
	id SERIAL PRIMARY KEY, 
	isLoggedIN BOOLEAN DEFAULT false,
	customer_id INTEGER UNIQUE REFERENCES customer(id)
);

-- 2
INSERT INTO customer (first_name, last_name) VALUES
('John', 'Doe'), ('Jerome','Lalu'), ('Lea', 'Rive');

SELECT * FROM customer;

3
INSERT INTO customer_profile (isLoggedIN, customer_id) VALUES
(true,
(SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Doe')
);

INSERT INTO customer_profile (customer_id) VALUES
((SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')
);

SELECT * FROM customer_profile;

-- 4
SELECT customer.first_name FROM customer
JOIN customer_profile ON customer.id = customer_profile.customer_id
WHERE customer_profile.isLoggedIN = true;

SELECT customer.first_name, customer_profile.isLoggedIN FROM customer_profile
RIGHT JOIN customer ON customer.id = customer_profile.customer_id;

SELECT COUNT(*) FROM customer_profile
WHERE isLoggedIN != true;

-- Part II
-- 1
CREATE TABLE book (
book_id SERIAL PRIMARY KEY,
title text NOT NULL,
author text NOT NULL
);

-- 2
INSERT INTO book (title, author)
VALUES 
('Alice In Wonderland', 'Lewish Carroll'),
('Harry Potter', 'J.K. Rowling'),
('To kill a mockingbird', 'Harper Lee');

SELECT * FROM book;

-- 3
CREATE TABLE student (
student_id SERIAL PRIMARY KEY,
name text NOT NULL UNIQUE,
age smallint CHECK (age <= 15) -- checks age
);

-- 4
INSERT INTO student (name, age)
VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

SELECT * FROM student;

-- 5 
CREATE TABLE library (
book_fk_id INT,
student_id INT,
borrowed_date DATE,
PRIMARY KEY (book_fk_id, student_id),
FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 6
INSERT INTO library (book_fk_id, student_id, borrowed_date)
SELECT book.book_id, student.student_id, '2022-02-15'
FROM book, student
WHERE book.title = 'Alice In Wonderland'
	AND student.name = 'John';

INSERT INTO library (book_fk_id, student_id, borrowed_date)
SELECT book.book_id, student.student_id, '2021-03-03'
FROM book, student
WHERE book.title = 'To kill a mockingbird'
	AND student.name = 'Bob';


INSERT INTO library (book_fk_id, student_id, borrowed_date)
SELECT book.book_id, student.student_id, '2021-05-23'
FROM book, student
WHERE book.title = 'Alice In Wonderland'
	AND student.name = 'Lera';

INSERT INTO library (book_fk_id, student_id, borrowed_date)
SELECT book.book_id, student.student_id, '2021-08-12'
FROM book, student
WHERE book.title = 'Harry Potter'
	AND student.name = 'Bob';

-- 7
SELECT * FROM library;

SELECT student.name, book.title FROM library 
JOIN student ON library.student_id = student.student_id
JOIN book ON library.book_fk_id = book.book_id;

SELECT AVG(student.age) FROM library 
JOIN student ON library.student_id = student.student_id
JOIN book ON library.book_fk_id = book.book_id
WHERE book.title = 'Alice In Wonderland';

DELETE FROM student WHERE name = 'John'; 

SELECT * FROM library;