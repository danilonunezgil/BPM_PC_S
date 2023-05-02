CREATE TABLE issues_bpm (
   id SERIAL PRIMARY KEY,
   title VARCHAR(255),
   link VARCHAR(255),
   score INTEGER,
   answer_count INTEGER,
   view_count INTEGER
);

select * from issues_bpm;
truncate table issues_bpm;
