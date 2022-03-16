-- 181. Employees Earning More Than Their Managers
-- #1.
select employee.name as Employee
from Employee as employee
    inner join Employee as manager on employee.managerId = manager.id
where employee.salary > manager.salary
