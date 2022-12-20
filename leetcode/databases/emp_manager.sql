# https://leetcode.com/problems/employees-earning-more-than-their-managers/


select ename as Employee from (select e.Name as ename, m.Name as mname, e.Salary as esal, m.Salary as msal from employee as e join employee as m on e.ManagerId = m.Id) as tmp where esal>msal;
