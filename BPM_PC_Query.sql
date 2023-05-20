CREATE TABLE BPM_PC_QUERY (
   id_discussion SERIAL PRIMARY KEY,
   topic VARCHAR(25),
   title VARCHAR(255),
   link VARCHAR(255),
   score INTEGER,
   answer_count INTEGER,
   view_count INTEGER,
   creation_date DATE,
   tags VARCHAR(255)
);
select * from BPM_PC_QUERY;
select *  from BPM_PC_QUERY where topic = 'jbpm';
select count(*) num_camunda from BPM_PC_QUERY where topic = 'jbpm';
truncate table BPM_PC_QUERY;
drop table BPM_PC_QUERY;