-- New Companies
-- #1. 

select Company.company_code
     , Company.founder
     , count(distinct Lead_Manager.Lead_Manager_code)
     , count(distinct Senior_Manager.Senior_Manager_code)
     , count(distinct Manager.Manager_code)
     , count(distinct Employee.Employee_code)

from Company
    inner join Lead_Manager on Company.company_code = Lead_Manager.company_code
    inner join Senior_Manager on Company.company_code = Senior_Manager.company_code
    inner join Manager on Company.company_code = Manager.company_code
    inner join Employee on Company.company_code = Employee.company_code
group by Company.company_code, Company.founder
    
