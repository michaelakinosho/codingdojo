USE friendships_schema;
SELECT *
FROM users;

INSERT INTO users (first_name,last_name,created_at,updated_at)
VALUES ('Amy','Giver',now(),now()),
		('Eli','Byers',now(),now()),
        ('Marky','Mark',now(),now()),
        ('Big','Bird',now(),now()),
        ('Kermit','The Frog',now(),now()),
        ('Busty','Rhymes',now(),now());

INSERT INTO friendships (user_id,friend_id,created_at,updated_at)
VALUES (1,2,now(),now()),
		(1,4,now(),now()),
        (1,6,now(),now()),
		(2,1,now(),now()),
        (2,3,now(),now()),
		(2,5,now(),now()),
        (3,2,now(),now()),
		(3,5,now(),now()),
        (4,3,now(),now()),
        (5,1,now(),now()),
		(5,5,now(),now()),
        (6,2,now(),now()),
		(6,3,now(),now());
        
SELECT users.first_name, users.last_name, Tfrdshps.friend_first_name, Tfrdshps.friend_last_name
FROM users LEFT JOIN (SELECT users.first_name as friend_first_name, users.last_name as friend_last_name, friendships.friend_id, friendships.user_id  FROM users JOIN friendships ON users.id = friendships.friend_id) AS Tfrdshps ON users.id = Tfrdshps.user_id;

SELECT Tfrdshps.friend_first_name, Tfrdshps.friend_last_name
FROM users LEFT JOIN (SELECT users.first_name as friend_first_name, users.last_name as friend_last_name, friendships.friend_id, friendships.user_id  FROM users JOIN friendships ON users.id = friendships.friend_id) AS Tfrdshps ON users.id = Tfrdshps.user_id WHERE users.id = 1;

SELECT COUNT(id) AS Friendships_Count FROM friendships;

SELECT concat(users.first_name,' ',users.last_name) AS Full_Name, COUNT(friendships.id) AS Friendships_Count FROM users LEFT JOIN friendships ON users.id = friendships.user_id GROUP BY Full_Name;

SELECT tMosfrdshps.Full_Name, MAX(tMosfrdshps.Friendships_Count) AS Most_Friends FROM (SELECT concat(users.first_name,' ',users.last_name) AS Full_Name, COUNT(friendships.id) AS Friendships_Count FROM users LEFT JOIN friendships ON users.id = friendships.user_id GROUP BY Full_Name) AS tMosfrdshps;

SELECT Tfrdshps.friend_first_name, Tfrdshps.friend_last_name
FROM users LEFT JOIN (SELECT users.first_name as friend_first_name, users.last_name as friend_last_name, friendships.friend_id, friendships.user_id  FROM users JOIN friendships ON users.id = friendships.friend_id) AS Tfrdshps ON users.id = Tfrdshps.user_id WHERE users.id =3 ORDER BY Tfrdshps.friend_first_name ;