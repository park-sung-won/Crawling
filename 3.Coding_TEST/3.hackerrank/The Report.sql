-- The Report
-- #1.

SELECT CASE WHEN Grades.grade < 8 THEN NULL 
            WHEN Grades.grade >= 8 THEN Students.name
            END AS name
     , Grades.grade AS grade
     , Students.marks AS marks
FROM Grades
    INNER JOIN Students ON Students.Marks >= Grades.Min_Mark 
                        AND Students.Marks <= Grades.Max_Mark
ORDER BY grade DESC, name, marks
