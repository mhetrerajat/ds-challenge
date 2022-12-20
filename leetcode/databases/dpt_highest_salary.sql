# https://leetcode.com/problems/department-highest-salary/


select d.Name as Department, e.Name as Employee, e.Salary from Department as d JOIN (select * from Employee as e where 1 > (select count(distinct e2.salary) from Employee as e2 where e2.salary > e.salary and e2.DepartmentId = e.DepartmentId)) as e ON d.Id = e.DepartmentId ;
