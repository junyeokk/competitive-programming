-- 코드를 입력하세요
SELECT fh.flavor from first_half fh, icecream_info icf
where fh.flavor = icf.flavor
and fh.total_order > 3000
and icf.ingredient_type = 'fruit_based'
order by fh.total_order desc