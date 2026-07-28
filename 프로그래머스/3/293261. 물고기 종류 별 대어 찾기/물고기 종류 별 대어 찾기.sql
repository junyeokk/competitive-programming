-- 코드를 작성해주세요
select f1.id, f2.fish_name, f1.length from fish_info as f1 join fish_name_info as f2
on f1.fish_type = f2.fish_type
and (f1.fish_type, f1.length) in (
select fish_type, max(length)
from fish_info
group by fish_type
)