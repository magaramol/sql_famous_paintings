-- first question 1. Fetch all the paintings which are not displayed in any museums

SELECT * from work
WHERE museum_id is null;


-- 2. Are there museums without any paintings?
SELECT * 
FROM museum 
WHERE museum_id NOT IN (
    SELECT DISTINCT museum_id 
    FROM work
);



