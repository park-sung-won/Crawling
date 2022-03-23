-- 620. Not Boring Movies
-- #1.

select *
from Cinema
where description not like '%boring%' and id % 2 = 1
order by rating desc
