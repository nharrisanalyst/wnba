begin;

create table if not exists  seasons (
  id integer PRIMARY KEY,
  year integer, 
  start_date date,
  end_date date
);

commit;