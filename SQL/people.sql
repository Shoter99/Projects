create table people (
	id bigint unsigned not null auto_increment,
	name varchar(100) not null,
	surname varchar(150) null,
	age int not null,
	primary key (id)
)engine=innodb
default charset=utf8
default collate=utf8_unicode_ci;
