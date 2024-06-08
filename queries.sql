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

 -- 4. Identify the paintings whose asking price is less than 50% of their regular price

SELECT  *
 from product_size
WHERE  sale_price < (regular_price*0.5)
;


-- 5. Which canvas size costs the most?
SELECT * from (SELECT a.size_id,a.sale_price,b.width,b.height,b.label,
rank() over (ORDER BY sale_price desc) as rnk
 from product_size a LEFT JOIN

canvas_size b on a.size_id=b.size_id
) t
WHERE t.rnk=1;
