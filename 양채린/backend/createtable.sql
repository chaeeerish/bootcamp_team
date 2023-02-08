SET foreign_key_checks = 0;
drop table if exists user;
create table user (
	id integer primary key auto_increment,
    username varchar(50) not null,
    drawing1 text,
    drawing2 text,
    result1 varchar(65535),
    result2 varchar(65535)
)

-- ----------------------------
select * from user;

SET foreign_key_checks = 1;