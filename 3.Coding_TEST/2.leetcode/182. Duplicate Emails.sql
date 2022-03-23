-- 182. Duplicate Emails
-- #1.

select email
from Person 
group by email
having count(id) > 1
