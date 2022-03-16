-- 180. Consecutive Numbers
-- #1.

select DISTINCT A.num as ConsecutiveNums
from Logs as A
    inner join Logs AS B ON A.id+1 = B.id
    inner join Logs AS C ON A.id+2 = C.id
where A.num = B.num and A.num = C.num


-- #2.

select distinct sub.num as ConsecutiveNums
from(
        select num 
            , lead(num, 1) over(order by id) as next2
            , lead(num, 2) over(order by id) as next3
        from Logs ) as sub

where sub.num = sub.next2
and sub.num = sub.next3
