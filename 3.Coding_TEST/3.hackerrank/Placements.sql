-- Placements
-- #1.

select st.name
from Friends as f
    inner join Packages as p1 on p1.id = f.id
    inner join Packages as p2 on p2.id = f.friend_id
    inner join Students as st on st.id = f.id
where p1.salary < p2.salary
order by p2.salary
