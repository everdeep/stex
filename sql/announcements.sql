CREATE TABLE announcements (
	id SERIAL PRIMARY KEY,
	code CHAR(3),
	time_posted VARCHAR(10),
	headline TEXT NOT NULL,
	pages INTEGER NOT NULL,
	pdf TEXT NOT NULL,
	date_added TIMESTAMPTZ DEFAULT NOW()
);
