-- 595. Big Countries
-- #1.

select name
     , population
     , area
from World
where area >= 3000000 or population >= 25000000
