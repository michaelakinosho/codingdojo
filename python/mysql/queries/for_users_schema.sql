USE users_schema;
SELECT *
FROM users;

INSERT INTO users (first_name,last_name,email,created_at,updated_at)
VALUES ('mike','olu','email@mike.com',now(),now()),
		('sanmi','son','code@mike.com',now(),now()),
		('boss','wife','bossmail@wife.com',now(),now());
        
SELECT *
FROM users;

SELECT *
FROM users
WHERE email = 'email@mike.com';

SELECT *
FROM users
WHERE email = 'bossmail@wife.com';

UPDATE users
SET last_name = 'Pancakes'
WHERE id = 3;

DELETE FROM users
WHERE id = 2;

SELECT *
FROM users
ORDER BY first_name;

SELECT *
FROM users
ORDER BY first_name DESC;




