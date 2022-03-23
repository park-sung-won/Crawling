-- Weather Observation Station 18
-- #1.

select round( abs(max(LAT_N) - min(LAT_N)) + abs(max(LONG_W) - min(LONG_W)) , 4 )
from STATION
