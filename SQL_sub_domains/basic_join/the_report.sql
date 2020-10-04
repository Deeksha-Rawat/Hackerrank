/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select case when Grade>=8 then Name else null end Name,Grade,Marks 

from 
     Students
     left join  Grades on Marks<=Max_Mark and Marks>=Min_Mark
    -- where Grade>=8
    order by Grade desc,Name asc,Marks asc 
     ;




