-- Naive Solution
-- TODO: Try another approach as joins are costly

SELECT *
FROM
  (SELECT students.student,
          other_students.student AS other_student,
          (students.score - other_students.score) AS diff
   FROM students
   JOIN students AS other_students ON students.student != other_students.student) AS tmp
WHERE tmp.diff >= 0
ORDER BY tmp.diff ASC
LIMIT 1;