# Write your MySQL query statement below
SELECT author_id AS id FROM `views`
WHERE viewer_id = author_id
GROUP BY author_id
ORDER BY author_id ASC;