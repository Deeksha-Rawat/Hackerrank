/*
Enter your query here.
*/
 SELECT MAX(months*salary)+' ',COUNT(months*salary)
FROM EMPLOYEE
WHERE (months*salary)= (SELECT MAX(months*salary) FROM EMPLOYEE);
/*UNION
SELECT COUNT(months*salary)
FROM EMPLOYEE
WHERE (months*salary)= (SELECT MAX(months*salary) FROM EMPLOYEE) ; 
*/