/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
/*select case when ((cnt%2)==0) then round(sum(LAT_N),4) else round((LAT_N),4) end as med
from
    (select * , rank()over(partition by id order by lat_n) rnk,count(id)over(partition by id) cnt
     from STATION
   )as al
 where rnk=cnt/2+1 and rnk=cnt/2        
 ;*/
 
 SELECT cast( (round(
   (SELECT MAX(lat_n) FROM
     (SELECT TOP 50 PERCENT lat_n
      FROM station ORDER BY lat_n) AS t),4)
 + round((SELECT MIN(lat_n) FROM
     (SELECT TOP 50 PERCENT lat_n 
      FROM station ORDER BY lat_N DESC) AS b),4 )
) / 2 as decimal(10,4)) ;





