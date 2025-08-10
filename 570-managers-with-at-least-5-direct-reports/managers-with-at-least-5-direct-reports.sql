# Write your MySQL query statement below
SELECT E1.name
FROM Employee E1
JOIN Employee E2
ON E1.id=E2.managerId
GROUP BY E2.managerId
HAVING COUNT(E2.managerId)>=5;