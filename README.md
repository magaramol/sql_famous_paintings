
# Famous Painting SQL Data Analysis

## Dataset Description

The Famous Paintings & Museum dataset provides extensive information about paintings, museums, artists, and related details.

### Data Source

The dataset is available on [Kaggle](https://www.kaggle.com/datasets/mexwell/famous-paintings).

### Tables

1. **work**: Information about the paintings.
   - Columns: painting_id, title, artist_id, asking_price, regular_price, museum_id, etc.
2. **product_size**: Details about the sizes of the paintings.
   - Columns: product_size_id, canvas_label, height, width.
3. **subject**: Information about the subjects of the paintings.
   - Columns: subject_id, subject_name.
4. **image_link**: Details about the image links of the paintings.
   - Columns: image_link_id, image_url, etc.
5. **museum**: Information about the museums.
   - Columns: museum_id, name, city, state, country, etc.
6. **museum_hours**: Details about the opening and closing hours of the museums.
   - Columns: museum_id, day, opening_time, closing_time.

## SQL Problems

### 1. Fetch all the paintings which are not displayed in any museums

```sql
SELECT * 
FROM work
WHERE museum_id IS NULL;
```

### 2. Are there museums without any paintings?

```sql
SELECT * 
FROM museum 
WHERE museum_id NOT IN (
    SELECT DISTINCT museum_id 
    FROM work
);
```

### 3. How many paintings have an asking price of more than their regular price?

```sql

SELECT count(*) from (SELECT 

*,sale_price-regular_price as diff

 from product_size) t

 WHERE t.diff>0
```


### 4. Identify the paintings whose asking price is less than 50% of their regular price


```sql
SELECT * from 
(SELECT  *,regular_price-sale_price as diff,
((regular_price-sale_price)/regular_price)*100 as cn
 from product_size
) t
WHERE t.cn>50

```

### 5. Which canvas size costs the most?


```sql

SELECT * from (SELECT a.size_id,a.sale_price,b.width,b.height,b.label,
rank() over (ORDER BY sale_price desc) as rnk
 from product_size a LEFT JOIN

canvas_size b on a.size_id=b.size_id
) t
WHERE t.rnk=1;

```

### 6. Delete duplicate records from `work`, `product_size`, `subject`, and `image_link` tables

### 7. Identify the museums with invalid city information

### 8. Identify and remove the invalid entry in the `museum_hours` table

### 9. Fetch the top 10 most famous painting subjects

### 10. Identify the museums open on both Sunday and Monday

### 11. Count the museums open every single day

### 12. Identify the top 5 most popular museums

### 13. Identify the top 5 most popular artists

### 14. Display the 3 least popular canvas sizes

### 15. Which museum is open for the longest during a day?

### 16. Which museum has the most number of the most popular painting style?

### 17. Identify the artists whose paintings are displayed in multiple countries

### 18. Display the country and city with the most number of museums

### 19. Identify the artist and museum with the most expensive and least expensive painting

### 20. Which country has the 5th highest number of paintings?

