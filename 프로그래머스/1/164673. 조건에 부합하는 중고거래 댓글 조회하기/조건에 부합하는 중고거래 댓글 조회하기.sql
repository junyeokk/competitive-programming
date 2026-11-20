-- 코드를 입력하세요
SELECT ugb.title, ugb.board_id, ugr.reply_id, ugr.writer_id, ugr.contents, ugr.created_date from used_goods_board as ugb, used_goods_reply as ugr
where ugb.board_id = ugr.board_id
and year(ugb.created_date) = '2022' and month(ugb.created_date) = '10'
order by ugr.created_date asc, ugb.title