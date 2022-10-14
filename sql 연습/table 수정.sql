drop table member;
create table member(
	no int(11) not null auto_increment,
    email varchar(100) not null,
    password varchar(64) not null,
    name varchar(100) not null,
    department varchar(100),
    primary key(no)
);

desc member;

alter table member add column juminbunho char(13) not null;
desc member;

alter table member drop juminbunho;
desc member;

alter table member add column juminbunho char(13) not null after email;
desc member;

alter table member change department department varchar(200) not null;
desc member;

alter table member add self_intro text;
desc member;

alter table member drop juminbunho;
desc member;

-- insert
insert
	into member(no, email, name, password, department)
values(null, 'whtjdgns00292@naver.com', '조성훈', password('1234'), '개발팀');
select * from member;

-- update
update member
	set email='whtjdgns00293@naver.com', password=password('4321')
where no = 2;
select * from member;

-- delete
delete
	from member
where no = 2;
select * from member;

-- tdansaction
select @@autocommit;
set autocommit=0;

insert
	into member(no, email, name, password, department)
values(null, 'whtjdgns00295@naver.com', '조성훈5', password('1234'), '개발팀');
select * from member;

commit;