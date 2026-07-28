-- 코드를 작성해주세요
select 
    year(differentiation_date) as year, 
    (select max(size_of_colony) 
     from ecoli_data e2
     where year(e2.differentiation_date) = year(e1.differentiation_date)) - e1.size_of_colony as year_dev, 
    id
from
    ecoli_data e1
order by year, year_dev