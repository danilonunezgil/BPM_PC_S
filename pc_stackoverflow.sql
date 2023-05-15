CREATE TABLE pc_stackoverflow (
   id SERIAL PRIMARY KEY,
   topic VARCHAR(25),
   title VARCHAR(255),
   link VARCHAR(255),
   score INTEGER,
   answer_count INTEGER,
   view_count INTEGER,
   creation_date DATE,
   tags VARCHAR(255)
);

select * from pc_stackoverflow;
select count(*) num_camunda from pc_stackoverflow where topic = 'camunda';
truncate table pc_stackoverflow;
drop table pc_stackoverflow;

