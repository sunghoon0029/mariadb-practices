show databases;
show tables;

insert
	into cartegory
values (null, '예술');
select * from cartegory;

insert
	into book
values (null, '현금과 예금관리', 36000, 5);
select * from book;

insert
	into member
values (null, '선태헌', '010-1234-5678', 'tjsxogjs@naver.com', 'bookmall');
select * from member;

insert
	into cart
values (null, 1, 0, 1, 2);
select * from cart;

insert
	into orders
values (null, 0, '서울특별시 서초구 서초대로74길 33', 1, 1);
select * from orders;

insert
	into orders_book
values (null, 2, 3, 1);
select * from orders_book;

-- 칼럼삭제 : alter table cart drop price;

-- 칼럼명 변경 : alter table orders_book
-- 		change column orders_order_no orders_no INT;
