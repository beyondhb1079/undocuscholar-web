-- Use this file to create the database.
create table scholarships(
  id integer primary key autoincrement,
  title text not null,
  amount integer,
  url text not null,
  deadline text
);
