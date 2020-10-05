/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE=(SELECT CODE FROM COUNTRY WHERE COUNTRY.CODE = CITY.COUNTRYCODE AND CONTINENT='Asia') ;