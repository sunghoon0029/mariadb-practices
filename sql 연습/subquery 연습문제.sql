-- 서브쿼리(SUBQUERY) SQL 문제입니다.

-- 문제1.
-- 현재 평균 연봉보다 많은 월급을 받는 직원은 몇 명이나 있습니까?
select count(b.salary) as '평균 이상 연봉 직원 수 '
  from employees a, salaries b
 where a.emp_no = b.emp_no
   and b.to_date = '9999-01-01'
   and b.salary > (select avg(salary)
				     from salaries
					where to_date = '9999-01-01');
	
-- 문제2. ???
-- 현재, 각 부서별로 최고의 급여를 받는 사원의 사번, 이름, 부서 연봉을 조회하세요. 단
-- 조회결과는 연봉의 내림차순으로 정렬되어 나타나야 합니다.

select a.dept_name, avg(c.salary) as avg_salary
  from departments a, dept_emp b, salaries c
 where a.dept_no = b.dept_no
   and b.emp_no = c.emp_no
   and b.to_date = '9999-01-01'
   and c.to_date = '9999-01-01'
group by dept_name;

select min(a.avg_salary)
  from (select a.dept_name, avg(c.salary) as avg_salary
		  from departments a, dept_emp b, salaries c
		 where a.dept_no = b.dept_no
		   and b.emp_no = c.emp_no
		   and b.to_date = '9999-01-01'
		   and c.to_date = '9999-01-01'
	  group by dept_name) a;

  select a.dept_name, avg(c.salary) as avg_salary
    from departments a, dept_emp b, salaries c
   where a.dept_no = b.dept_no
     and b.emp_no = c.emp_no
     and b.to_date = '9999-01-01'
     and c.to_date = '9999-01-01'
group by dept_name
  having avg_salary = (select min(a.avg_salary)
						 from (select a.dept_name, avg(c.salary) as avg_salary
								 from departments a, dept_emp b, salaries c
								where a.dept_no = b.dept_no
								  and b.emp_no = c.emp_no
							      and b.to_date = '9999-01-01'
							      and c.to_date = '9999-01-01'
						     group by dept_name) a);
  
 
select b.dept_name, a.emp_no, a.first_name, salary
  from employees a, departments b, dept_emp c
 where a.emp_no = c.emp_no
   and c.dept_no = b.dept_no
   and c.to_date = '9999-01-01'
   and salray = (select max(salary)
		           from salaries
				  where to_date = '9999-01-01');
  

-- 문제3. !!!
-- 현재, 자신의 부서 평균 급여보다 연봉(salary)이 많은 사원의 사번, 이름과 연봉을 조회하세요
select a.emp_no, a.first_name, b.salary
  from employees a, salaries b
 where a.emp_no = b.emp_no
   and b.to_date = '9999-01-01'
   and b.salary > (select avg(salary)
					 from salaries
					where to_date = '9999-01-01')
order by b.salary desc;

-- 문제4.
-- 현재, 사원들의 사번, 이름, 매니저 이름, 부서 이름으로 출력해 보세요.
select a.emp_no, a.first_name, b.title, c.dept_name
  from employees a,
	   titles b,
       departments c
 where a.emp_no = b.emp_no
   and b.to_date = '9999-01-01';

-- 문제5. ???
-- 현재, 평균연봉이 가장 높은 부서의 사원들의 사번, 이름, 직책, 연봉을 조회하고 연봉 순으로
-- 출력하세요.
select max(avg(salary))
  from salaries;
  
select a.emp_no, a.first_name, b.title, c.salary
  from employees a, titles b, salaries c
 where a.emp_no = b.emp_no
   and b.to_date = '9999-01-01'
   and c.salary = (select max(avg(salary))
					 from salaries)
group by c.salary;
   

-- 문제6.
-- 평균 연봉이 가장 높은 부서는?
select avg(salary)
  from salaries;
  
select a.dept_name, max(b.salary)
  from departments a, salaries b, dept_emp c
 where a.dept_no = c.dept_no
   and b.to_date = c.to_date
   and b.to_date = '9999-01-01'
   and b.salary = (select avg(salary)
					 from salaries);


-- 문제7. ???
-- 평균 연봉이 가장 높은 직책?
select max(salary)
  from salaries;
  
select a.title, b
  from titles a,
       (select max(salary)
		  from salaries) b;

-- 문제8.
-- 현재 자신의 매니저보다 높은 연봉을 받고 있는 직원은?
-- 부서이름, 사원이름, 연봉, 매니저 이름, 메니저 연봉 순으로 출력합니다.
