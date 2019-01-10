# https://leetcode.com/problems/trips-and-users/<Paste>


select Request_at as 'Day', ROUND(SUM((CASE WHEN tmp.status = 'completed' THEN 0 else 1 END)) / (count(*)), 2) as 'Cancellation Rate' from (select Request_at, Status from trips, users where Request_at between "2013-10-01" and "2013-10-03" and trips.Client_id = users.Users_id and users.role = 'client' and Banned = 'NO') as tmp group by tmp.Request_at;
