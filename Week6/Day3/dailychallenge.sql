-- # Daily Challenge: Tables Relationships
-- # 1.Create 2 tables : Customer and Customer profile. 
-- They have a One to One relationship. 
-- Use all the types of Joins to display the data.

-- CREATE TABLE customer(
-- customer_id SERIAL,
-- customer_name VARCHAR(50) NOT NULL,
-- PRIMARY KEY (customer_id)
-- );

-- CREATE TABLE customer_profile(
-- pk_customer_id INTEGER NOT NULL,
-- customer_character TEXT NOT NULL,
-- PRIMARY KEY (pk_customer_id),
-- CONSTRAINT fk_customer_id FOREIGN KEY (pk_customer_id) REFERENCES customer (customer_id)
-- );

-- INSERT INTO customer(customer_name) VALUES 
-- ('John'),
-- ('Sam'),
-- ('Anne'),
-- ('Linda'),
-- ('Sarah');

-- INSERT INTO customer_profile(pk_customer_id, customer_character) VALUES
-- ((SELECT customer_id FROM customer WHERE customer_name = 'Sarah'), 'She is very kind and helps us to improve our services.'),
-- ((SELECT customer_id FROM customer WHERE customer_name = 'Sam'), 'He has a very bad temper.');

-- SELECT customer.customer_name, customer_profile.customer_character as character
-- FROM customer
-- FULL OUTER JOIN customer_profile
-- ON customer.customer_id = customer_profile.pk_customer_id;



-- #2.Create 2 other tables : Product and Order. 
-- Order is a table with a Many to Many relationship with the Customer and Product tables. 
-- Use all the types of Joins to display the data.

-- CREATE TABLE customer(
-- customer_id SERIAL,
-- customer_name VARCHAR(50) NOT NULL,
-- PRIMARY KEY (customer_id)
-- );

-- CREATE TABLE customer_profile(
-- pk_customer_id INTEGER NOT NULL,
-- customer_character TEXT NOT NULL,
-- PRIMARY KEY (pk_customer_id),
-- CONSTRAINT fk_customer_id FOREIGN KEY (pk_customer_id) REFERENCES customer (customer_id)
-- );

-- INSERT INTO customer(customer_name) VALUES 
-- ('John'),
-- ('Sam'),
-- ('Anne'),
-- ('Linda'),
-- ('Sarah');

-- INSERT INTO customer_profile(pk_customer_id, customer_character) VALUES
-- ((SELECT customer_id FROM customer WHERE customer_name = 'Sarah'), 'She is very kind and helps us to improve our services.'),
-- ((SELECT customer_id FROM customer WHERE customer_name = 'Sam'), 'He has a very bad temper.');

-- SELECT customer.customer_name, customer_profile.customer_character as character
-- FROM customer
-- FULL OUTER JOIN customer_profile
-- ON customer.customer_id = customer_profile.pk_customer_id;


-- CREATE TABLE product (
-- item_id SERIAL,	
-- product_name VARCHAR(30) NOT NULL,
-- PRIMARY KEY (item_id)
-- );

-- INSERT INTO product(product_name) VALUES
-- ('Chairs'),
-- ('Table'),
-- ('Fan'),
-- ('Bottle'),
-- ('Hammer'),
-- ('Nails');

-- CREATE TABLE item_order (
-- customer_id INTEGER NOT NULL,
-- item_id INTEGER NOT NULL,
-- number_order INTEGER NOT NULL,
-- PRIMARY KEY (customer_id, item_id),
-- FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE,
-- FOREIGN KEY (item_id) REFERENCES product(item_id) ON UPDATE CASCADE
-- );

-- INSERT INTO item_order(customer_id, item_id, number_order) VALUES
-- ((SELECT customer_id FROM customer  WHERE customer_name = 'Sam'), (SELECT item_id FROM product WHERE product_name = 'Chairs'), 5),
-- ((SELECT customer_id FROM customer  WHERE customer_name = 'Sarah'), (SELECT item_id FROM product WHERE product_name = 'Bottle'), 2),
-- ((SELECT customer_id FROM customer  WHERE customer_name = 'John'), (SELECT item_id FROM product WHERE product_name = 'Hammer'), 1);
