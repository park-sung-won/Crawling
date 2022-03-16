-- Symmetric Pairs
-- #1.

SELECT X, Y
FROM Functions
WHERE X = Y
GROUP BY X , Y
HAVING count(*) = 2

UNION

SELECT f1.X , f1.Y
FROM Functions AS f1
    INNER JOIN Functions AS f2 ON f1.X = f2.Y AND f2.X = f1.Y
WHERE f1.X < f1.Y
