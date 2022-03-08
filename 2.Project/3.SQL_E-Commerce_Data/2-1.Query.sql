-- 고객 타입별 평균 거래주기(단위:일)
SELECT c.segment, avg(avg_date)
FROM 
                        (with p1 as(
                        select customer_id, order_date, next_date,         datediff (next_date,order_date) as count_date
                                                from 
                                                        (SELECT customer_id, order_date, 
                                                                                lead(order_date,1) OVER (PARTITION BY customer_id ORDER BY customer_id,order_date) AS next_date
                                                        FROM 
                                                                                (select distinct order_date, customer_id from records) as a)as b)
                                                        
                        select rec.segment, p1.customer_id,  sum(count_date)/count(count_date) as avg_date
                        from p1
                        JOIN records as rec on p1.customer_id = rec.customer_id
                        group by p1.customer_id, rec.segment) as c
group by c.segment;
