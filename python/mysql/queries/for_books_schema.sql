USE books_schema;
SELECT *
FROM authors;

INSERT INTO authors (first_name,last_name,created_at,updated_at)
VALUES ('Jane','Austen',now(),now()),
		('Emily','Dickinson',now(),now()),
        ('Fyodor','Dostoevsky',now(),now()),
        ('William','Shakespeare',now(),now()),
        ('Lau','Tzu',now(),now());
        
SELECT *
FROM books;

INSERT INTO books (title,num_of_pages,created_at,updated_at)
VALUES ('C Sharp',100,now(),now()),
		('Java',200,now(),now()),
        ('Python',300,now(),now()),
        ('PHP',400,now(),now()),
        ('Ruby',500,now(),now());
        
UPDATE books
SET title = 'C#'
WHERE title = 'C Sharp';

UPDATE authors
SET first_name = 'Bill'
WHERE id = 4;

INSERT INTO favorites (author_id, book_id, created_at,updated_at)
VALUES (1,1,now(),now()),
		(1,2,now(),now());
        
INSERT INTO favorites (author_id, book_id, created_at,updated_at)
VALUES (2,1,now(),now()),
		(2,2,now(),now()),
        (2,3,now(),now());

INSERT INTO favorites (author_id, book_id, created_at,updated_at)
VALUES (3,1,now(),now()),
		(3,2,now(),now()),
        (3,3,now(),now()),
        (3,4,now(),now());
        
SELECT authors.first_name, authors.last_name FROM authors JOIN favorites ON authors.id = favorites.author_id WHERE favorites.book_id = 3;

DELETE
FROM favorites
WHERE author_id = 2 AND book_id = 3;

INSERT INTO favorites (author_id, book_id, created_at,updated_at)
VALUES (5,2,now(),now());

SELECT title
FROM books JOIN favorites ON books.id = favorites.book_id WHERE favorites.author_id = 3;

SELECT books.title, books.id, tFAV_AUTH.author_full_name
FROM books JOIN (SELECT authors.id, concat(authors.first_name," ",authors.last_name) AS author_full_name, book_id FROM authors JOIN favorites ON  authors.id = favorites.author_id WHERE favorites.author_id = 3) AS tFAV_AUTH ON books.id = tFAV_AUTH.book_id;

SELECT concat(authors.first_name," ",authors.last_name) AS author_full_name, authors.id, tFAV_BOOK.title
FROM authors JOIN (SELECT books.title, books.id, favorites.author_id FROM books JOIN favorites ON books.id = favorites.book_id WHERE favorites.book_id = 5) AS tFAV_BOOK ON authors.id = tFAV_BOOK.author_id;
