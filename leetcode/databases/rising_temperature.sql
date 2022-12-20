# https://leetcode.com/problems/rising-temperature/submissions/


select w.id as Id from weather as w join weather w2 on DATEDIFF(w.RecordDate, w2.RecordDate) = 1 and w.Temperature > w2.Temperature;
