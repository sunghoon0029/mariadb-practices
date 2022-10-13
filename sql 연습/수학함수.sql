-- 함수: 수학

-- abs
select abs(1), abs(-1);

-- ceil
select ceil(3.14), ceiling(3.14);

-- floor
select floor(3.14);

-- mod
select mod(10, 3);

-- round(x): x에 가장 근접한 정수
-- round(x, d): x값 중에 소수점 d자리에 가장 근접한 실수
select round(1.498), round(1.498,1), round(1.498, 0);

-- power(x, y), pow(x, y): x의 y승
select power(2,10), pow(2, 10);

-- sign(x): 양수는 1, 음수는 -1, 0은 0 으로 출력
select sign(20), sign(-10);

-- greatest(x, y, ...), least(x, y, ....)
select greatest(10, 40, 20, 50), least(10, 40, 20, 50);
select greatest('b', 'A', 'C', 'B'), greatest('hello','hela','hell');
