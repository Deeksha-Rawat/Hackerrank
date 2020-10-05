/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select country.continent, round(sum(city.population)/count(distinct city.id),0) average
from country
join city on country.code=city.countrycode
group by country.continent

;