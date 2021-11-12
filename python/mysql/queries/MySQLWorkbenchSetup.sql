USE twitter;
INSERT INTO users (first_name,last_name,handle,birthday,created_at,updated_at)
VALUES ('michael','akinosho','olumike','1974-12-04',now(),now());

SELECT *
FROM users
WHERE last_name = 'akinosho';

UPDATE users
SET created_at = now()-6, updated_at = now()
WHERE last_name = 'akinosho';

DELETE FROM users
WHERE last_name = 'akinosho';

SELECT *
FROM users
WHERE last_name = 'akinosho';