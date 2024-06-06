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

-- 3. How many paintings have an asking price of more than their regular price?

SELECT count(*) from (SELECT 

*,sale_price-regular_price as diff

 from product_size) t

 WHERE t.diff>0;
 