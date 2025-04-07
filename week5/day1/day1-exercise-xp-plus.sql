-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = gabby
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'en_US.UTF-8'
--     LC_CTYPE = 'en_US.UTF-8'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

CREATE TABLE students(
 student_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 birth_date DATE NOT NULL
)

ALTER TABLE students RENAME COLUMN actor_id TO student_id;
SELECT * FROM students

SET datestyle = 'DMY';

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Marc','Benichou','02/11/1998'),
('Yoan','Cohen','3/12/2010'),
('Lea','Benichou','27/07/1987'),
('Amelia','Dux','07/04/1996'),
('David','Grez','14/06/2003'),
('Omer','Simpson','03/10/1980');

COMMIT;

SELECT * FROM students

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Gabby','Zuckerman','24/04/1997');
-- Execute then COMMIT
COMMIT;

-- 1
SELECT * FROM students

-- 2
SELECT first_name, last_name FROM students

-- 3
SELECT first_name, last_name FROM students WHERE student_id = 2

-- 4
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc'

-- 5
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'

-- 6
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%'
-- % represents any number of characters before or after "a".
-- LIKE searching in text fields - % = zero or more and _ = exactly one character.

-- 7
SELECT first_name, last_name FROM students WHERE first_name LIKE 'A%'

-- 8
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a'

-- 9 
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_'

-- 10
SELECT first_name, last_name FROM students WHERE student_id IN (1, 3);
-- IN matches rows to the numbers provided

-- 11
SELECT first_name, last_name, birth_date FROM students WHERE birth_date >= '01/01/2000'







