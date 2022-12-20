
# https://leetcode.com/problems/second-highest-salary/submissions/

select ifnull((select Salary from (select Salary from employee group by Salary) as tmp order by salary desc limit 1,1), null) as SecondHighestSalary;
