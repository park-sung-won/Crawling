-- 196. Delete Duplicate Emails
-- #1.

DELETE A
FROM Person AS A
    JOIN Person AS B ON A.email = B.email
WHERE A.id > B.id
