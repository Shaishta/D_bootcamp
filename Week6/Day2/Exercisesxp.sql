#exercisexp
#Exercise 1 : Items And Customers

-- public=# select * from items order by price ASC;
-- public=# select * from items where price >= 80 ORDER BY price ASC;
-- public=# select first_name, last_name from customers order by first_name limit 3;
-- public=# select last_name from customers order by last_name DESC;

-- CREATE TABLE purchases(customer_id int, item_id int, FOREIGN KEY (customer_id) references customers(id), FOREIGN KEY(item_id) references items(item_id));
-- INSERT INTO purchases(customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Scott'),(SELECT item_id FROM items WHERE item_name = 'Small desk'));
-- INSERT INTO purchases(customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Greg'), (SELECT item_id FROM items WHERE item_name = 'Fan'));
-- INSERT INTO purchases(customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Sandra'), (SELECT item_id FROM items WHERE item_name = 'Large desk')); 
-- INSERT INTO purchases(customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Melanie'), (SELECT item_id FROM items WHERE item_name = 'chair'));
-- INSERT INTO purchases(customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Trevor'), (SELECT item_id FROM items WHERE item_name = 'chair'));

-- public=# select * from purchases; 
-- public=# select customers.first_name, customers.last_name, purchases.customer_id, purchases.item_id FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
-- public=# select customers.first_name, customers.last_name, purchases.customer_id, purchases.item_id FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id where id = 4;
-- public=# select customers.first_name, customers.last_name, purchases.customer_id, purchases.item_id FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id where item_id = 1 or item_id = 2;

-- INSERT INTO items(item_name, price) VALUES ('Hard drive', 500); INSERT INTO purchases (customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Scott'), (SELECT item_id FROM items WHERE item_name = 'Hard drive')); 

-- public=# select customers.first_name FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
-- public=# select customers.last_name FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
-- public=# select item_name FROM items INNER JOIN purchases ON items.item_id = purchases.customer_id;

# Exercise 2 : Dvdrental Database


-- select * from customer;

-- select first_name, last_name from customer as full_name;

-- select distinct create_date from customer;

-- select * from customer order by first_name desc;

-- select film_id, title, description, release_year, rental_rate from film order by rental_rate;

-- select address, phone from address where district = 'Texas';

-- select * from film where film_id = 15 or film_id = 150;

-- select film_id, title, description, length, rental_rate from film where title = 'Titanic';

-- select title from film; select film_id, title, description, length, rental_rate from film where title ilike 'ti%';

-- select title , rental_rate from film order by rental_rate ASC limit 10;

-- select title , rental_rate from film order by rental_rate offset 10 rows fetch next 10 rows only;

-- select customer.customer_id, customer.first_name, payment.amount, payment.payment_date from customer inner join payment on payment.customer_id = customer.customer_id order by customer_id; select film.film_id, film.title, inventory.film_id from film inner join inventory on inventory.film_id = film.film_id;

-- select title, film_id from film where film_id not in (select film_id from inventory);

-- select city.city, country.country_id, country.country from city inner join country on country.country_id = city.country_id;

-- select customer.first_name, customer.last_name, payment.customer_id, payment.amount, payment.payment_date, payment.staff_id from customer left join payment on payment.customer_id = customer.customer_id order by payment.staff_id;
