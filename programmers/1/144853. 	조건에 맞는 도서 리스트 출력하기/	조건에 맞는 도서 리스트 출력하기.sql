-- 코드를 입력하세요
SELECT book_id, published_date from book
where published_date between '2021-01-01' and '2021-12-31'
-- where published_date >= '2021-01-01' and published_date <= '2021-12-31'
and category = '인문'