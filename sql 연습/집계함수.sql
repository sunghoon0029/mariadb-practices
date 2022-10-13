-- 집계쿼리: select 절에 그룹함수(avg, max, min, count, sum, ...)가 적용된 경우

select avg(salary), sum(salary)
  from salaries;
  
-- select절에 그룹함수가 있는 경우, 어떤 컬럼도 select 절에 올 수 없다
-- emp_no는 아무 의미 없다(오류)
select avg(salary), emp_no
  from salaries;
  
-- query 순서
-- 1) from: 접근 테이블 확인
-- 2) where: 조건에 맞는 row를 선택
-- 3) 집계
-- 4) projection 
select avg(salary)
  from salaries
where emp_no='10060';

-- group by에 참여하고 있는 칼럼은 projection이 가능하다(select 절에 올 수 있다)
select emp_no, avg(salary)
  from salaries
group by emp_no;

-- having
-- 집계결과(결과 임시 테이블)에서 row를 선택해야 하는 경우
-- 이미 where 절은 실행이 되었기 때문에 having 절에 이 조건을 주어야 한다
select emp_no, avg(salary) as avg_salary
  from salaries
group by emp_no
  having avg_salary > 60000
order by avg_salary desc;