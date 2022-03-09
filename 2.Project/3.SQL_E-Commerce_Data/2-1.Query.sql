-- 고객 타입별 평균 거래주기(단위:일)

<작성 쿼리>
select c.segment, avg(avg_date)
from 
                        (with p1 as(
                        select customer_id
				, order_date
				, next_date
				, datediff (next_date,order_date) as count_date
			        from 
			        (select customer_id
				 	, order_date
					, LEAD(order_date,1) over (partition by customer_id order by customer_id,order_date) as next_date
		                        from 
		                        (select distinct order_date
						, customer_id 
						from records) as a)as b)
                                                        
                        select rec.segment
				, p1.customer_id
				,  sum(count_date)/count(count_date) as avg_date
			        from p1
				   inner join records as rec on p1.customer_id = rec.customer_id
                        group by p1.customer_id, rec.segment) as c
group by c.segment;

------------------------------------------------------------------------------------------------------------------------------------
-- 상품 서브 카테고리 별 평균 거래주기 (단위:일)

<작성쿼리>
select c.sub_category
	, avg(avg_date)
	from 
        (with p1 as(
        select customer_id
		, order_date
		, next_date
		, datediff (next_date,order_date) as count_date
                from (select customer_id
				, order_date
				, lead(order_date,1) over (partition by customer_id order by customer_id,order_date) as next_date
                from (select distinct order_date
					, customer_id 
					from records) as a)as b)
                                                        
                        select rec.sub_category
				, p1.customer_id
				,  sum(count_date)/count(count_date) as avg_date
			        from p1
				   	inner JOIN records as rec on p1.customer_id = rec.customer_id
		                    group by p1.customer_id, rec.sub_category) as c
group by c.sub_category;

------------------------------------------------------------------------------------------------------------------------------------
-- 고객타입별 월 주문수 합계 (단위:건)

<작성쿼리>
select date_format(order_date, '%Y-%m') as YM
			,sum(case when segment = 'Consumer' then cnt_orders end)  as Consumer
			,sum(case when segment = 'Home Office' then cnt_orders end) as HomeOffice
			,sum(case when segment = 'Corporate' then cnt_orders end) as Corporate

from customer_stats as c
		inner join records as r on c.customer_id =  r.customer_id
group by date_format(order_date, '%Y-%m')
order by YM ;

------------------------------------------------------------------------------------------------------------------------------------
-- 전체 매출액 대비 매출총이익률 (단위 : %)

<작성쿼리>
select date_format(order_date, '%Y-%m') as YM
			, sum(profit)/sum(sum_sales) * 100 as rate_profit_sum

from customer_stats as c
		inner	join records as r on c.customer_id =  r.customer_id
group by date_format(order_date, '%Y-%m')
order by YM ;

------------------------------------------------------------------------------------------------------------------------------------
-- 전체 고객 대상 재구매 경험 여부

<작성 쿼리>
select sum(retention_num) as '1' 
			,count(retention_num)-sum(retention_num) as '0'
			from( select customer_id, 
							case when DATEDIFF(last_order_date, first_order_date)/cnt_orders != 0 then 1 
							else 0 end as retention_num
							from customer_stats) as x;
              
------------------------------------------------------------------------------------------------------------------------------------
-- 신규 고객 유입현황

1. 월별 신규 고객 유입현황
<작성 쿼리>
select date_format(first_order_date, '%Y-%m') as YM
			, count(first_order_date) as count_first
			from customer_stats
group by date_format(first_order_date, '%Y-%m')
order by YM;


2. 고객타입별 신규고객 유입현황
<작성 쿼리>
select distinct YM
        , count(case when Consumer = 1 then customer_id end) as Consumer
        , count(case when HomeOffice = 1 then customer_id end) as HomeOffice
        , count(case when Corporate = 1 then customer_id end) as Corporate

from(select date_format(first_order_date, '%Y-%m') as YM
					, c.customer_id
					, count(distinct case when segment = 'Consumer' then first_order_date end) as Consumer
					, count(distinct case when segment = 'Home Office' then first_order_date end) as HomeOffice
					, count(distinct case when segment = 'Corporate' then first_order_date end) as Corporate

			   from customer_stats as c
				   inner join records as r on c.customer_id =  r.customer_id

   group by date_format(first_order_date, '%Y-%m'),c.customer_id
   order by YM
   ) as PPP
group by YM
