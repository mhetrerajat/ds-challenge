# https://leetcode.com/problems/not-boring-movies/submissions/


select * from cinema where mod(id, 2) != 0 and description not like 'boring' order by rating desc;
