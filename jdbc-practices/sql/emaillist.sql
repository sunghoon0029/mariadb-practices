desc pet;

insert into pet values('딸랑이', '조성훈', 'dog', 'm', '2020-10-18', null);
delete from pet where name = '딸랑이';

select name, owner, species, gender, date_format(birth, '%Y-%m-%d') from pet;

-- emaillist sql 연습

-- insert
insert into emaillist values(null, '안', '대혁', 'dkseogur@gmail.com');
insert into emaillist values(null, '둘', '리', 'dooly@gmail.com');

-- select
select first_name, last_name, email from emaillist order by no desc;
select * from emaillist;

-- delete
delete from emaillist where email = 'dkseogur@gmail.com';

desc emaillist;

select * from dept;

insert 
 into dept
values(null, '조', '성훈', 'whtjdgns0029');

delete
  from dept 
 where no = 8;

update dept
  set name = '전략기획'
where no = 4; 