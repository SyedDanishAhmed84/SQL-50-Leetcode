# Write your MySQL query statement below
SELECT E.name , B.bonus
FROM Employee e
LEFT JOIN bonus B
ON E.empId=B.empId
WHERE B.bonus < 1000 OR B.bonus IS null;