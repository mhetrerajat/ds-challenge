# https://leetcode.com/problems/duplicate-emails/

select tmp.Email from (select count(*) as count, Email from Person group by Email) as tmp where tmp.count >= 2;
