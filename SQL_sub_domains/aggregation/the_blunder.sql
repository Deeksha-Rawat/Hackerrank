/*
Enter your query here.
*/
SELECT CEIL(AVG(Salary)-AVG(TO_NUMBER(REPLACE(TO_CHAR(Salary),'0',''))))
FROM EMPLOYEES;
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/