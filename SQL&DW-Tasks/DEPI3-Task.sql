--USE CompanyDB;

--SELECT fname, lname, salary, dno, salary + (salary*30)/100 AS new_salary
--FROM Employee;

--SELECT fname,
--		lname,
--		salary,
--		CASE WHEN salary < 1000 THEN 'LOW'
--			WHEN SALARY > 1000 and SALARY < 2000 THEN 'MID'
--			WHEN salary > 2000 THEN 'HIGH'
--			ELSE 'Undefined'
--			END AS salType
--	from Employee;

--SELECT fname,lname,salary,
--		CASE WHEN salary < 1000 AND dno = 20 THEN 'Low - Dep20'
--			WHEN salary > 2000 AND dno = 30 THEN 'High - Dep30'
--			ELSE 'Undefined'
--			END AS 'Salary - Department'
--	FROM Employee;

--SELECT e.Fname, e.Lname, e.Address, d.Dname
--FROM Employee e
--JOIN Department d
--ON(d.DNum=e.Dno)
--WHERE d.Dname = 'DP3';

--SELECT fname, lname, address, dno, dname FROM Employee,Department where Dname = 'DP3';

SELECT e.fname, e.lname, e.ssn, e.superssn, m.ssn, m.fname, m.lname
FROM Employee e
JOIN Employee m
ON (e.superssn = m.ssn);+