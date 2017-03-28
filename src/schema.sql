drop table if exists sox_ping_log;
CREATE TABLE sox_ping_log(
  created datetime not null,
  protocol varchar(255) not null,
  destination varchar(255) not null,
  status boolean not null
);

create index sox_ping_log_created on sox_ping_log (created);
