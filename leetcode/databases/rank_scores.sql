
# https://leetcode.com/problems/rank-scores/

select tmp.Score as Score, CAST(tmp.rnk as UNSIGNED) as 'Rank' from (select Score, (@r:=@r+1) as rnk FROM (SELECT distinct(Score) from Scores) as ds, (SELECT @r:=0) as r order by Score DESC) as tmp right join scores on tmp.Score = scores.Score order by Score DESC;
