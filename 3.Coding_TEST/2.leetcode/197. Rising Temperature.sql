-- 197. Rising Temperature
-- #1.

SELECT now.id AS id
FROM Weather AS now
    INNER JOIN Weather AS previous ON now.recordDate = DATE_ADD(previous.recordDate , INTERVAL 1 DAY)
WHERE (now.temperature - previous.temperature) > 0
