-- Write your query below
SELECT s.seller_name 
FROM seller s
Where s.seller_id not in (
    SELECT o.seller_id
    from orders o
    WHERE EXTRACT(YEAR FROM o.sale_date) = 2020
)
order by s.seller_name;