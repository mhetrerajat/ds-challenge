# https://leetcode.com/problems/nth-highest-salary/submissions/



CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
	set N = N-1;
	  RETURN (
		      # Write your MySQL query statement below.
		      select ifnull((select Salary from (select Salary from employee group by Salary) as tmp order by salary desc limit 1 offset N), null)
		  );
		END




