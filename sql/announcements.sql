CREATE TABLE announcements (
	id SERIAL PRIMARY KEY,
	code CHAR(3),
	published VARCHAR(10),
	headline VARCHAR(50) NOT NULL,
	pages INTEGER NOT NULL,
	pdf VARCHAR(50) NOT NULL
);
