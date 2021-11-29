-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

-- CREATE DATABASE "Hollywood"
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Mauritius.1252'
--     LC_CTYPE = 'English_Mauritius.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;
-- CREATE TABLE actors(actor_id SERIAL PRIMARY KEY, first_name VARCHAR (50) NOT NULL, last_name VARCHAR (100) NOT NULL, age DATE NOT NULL, number_oscars SMALLINT NOT NULL)
-- INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES ('Matt','Damon','1970/10/08', 5), ('George',' Clooney','1961/05/06', 2), ('Scarlett ','Johansson','1984/11/22', 0), ('Meryl','Streep','1949/06/22', 0), ('Sean', 'Penn', '1960/08/17', 2), ('Tom', 'Hanks','1956/07/09', 2 ), ('Michael', 'Caine', '1933/03/14', 2), ('Daniel', 'Day-Lewis', '1957/04/29', 3),('Cate', 'Blanchett', '1969/05/14', 2), ('Johnny', 'Depp', '1963/06/09', 0);
-- SELECT COUNT(first_name) FROM actors;
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES (null,null,null,null)
