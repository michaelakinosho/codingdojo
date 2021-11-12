USE dojos_and_ninjas_schema;

INSERT INTO dojos (name,created_at,updated_at)
VALUES ('Beijing',now(),now()),
		('Shanghai',now(),now()),
		('Shenzhen',now(),now());
        
DELETE FROM dojos;

INSERT INTO dojos (name,created_at,updated_at)
VALUES ('Shoalin',now(),now()),
		('Wu-Tang',now(),now()),
		('Shang-Chi',now(),now());
        
SELECT *
FROM dojos;

-- Source of SQL function to add dojo_id using dojo name
-- https://stackoverflow.com/questions/3075147/select-into-variable-in-mysql-declare-causes-syntax-error
-- Since the dojo name is known but not the id, using the known name to pass the
-- id to the ninjas table, ninjas table needs the dojo id and not the dojo name
SELECT id INTO @dojo_id FROM dojos WHERE name = 'Shoalin';
INSERT INTO ninjas (first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES ('mike','akinosho',47,now(),now(),@dojo_id),
		('ade','akinosho',23,now(),now(),@dojo_id),
        ('danielle','akinosho',15,now(),now(),@dojo_id);

SELECT id INTO @dojo_id FROM dojos WHERE name = 'Wu-Tang';
INSERT INTO ninjas (first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES ('ruth','akinosho',75,now(),now(),@dojo_id),
		('will','akinosho',10,now(),now(),@dojo_id),
        ('temi','akinosho',9,now(),now(),@dojo_id);

SELECT id INTO @dojo_id FROM dojos WHERE name = 'Shang-Chi';
INSERT INTO ninjas (first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES ('francis','akinosho',18,now(),now(),@dojo_id),
		('wale','akinosho',46,now(),now(),@dojo_id),
        ('toun','adediji',67,now(),now(),@dojo_id);

SELECT id INTO @dojo_id FROM dojos WHERE name = 'Shoalin';
SELECT *
FROM ninjas
WHERE dojo_id = @dojo_id;

SELECT id INTO @dojo_id FROM dojos WHERE name = 'Shang-Chi';
SELECT *
FROM ninjas
WHERE dojo_id = @dojo_id;

SELECT dojo_id, MAX(id) AS maxID INTO @dojo_id, @maxID FROM ninjas;
SELECT *
FROM dojos
WHERE id = @dojo_id;