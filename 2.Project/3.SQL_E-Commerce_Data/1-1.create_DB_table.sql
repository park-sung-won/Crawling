
create database e_commerce;
use e_commerce;

create table customer_stats(
customer_id varchar(100) primary key,
first_order_date date null,
last_order_date date null,
cnt_orders int null,
sum_sales float null
);

create table records(
order_date date null,
order_id varchar(1000) null,
ship_mode varchar(1000) null,
customer_id varchar(1000) primary key,
segment varchar(100) null,
country varchar(100),
city varchar(100),
state varchar(100),
postal_code int,
region varchar(100),
product_id varchar(100),
category varchar(100),
sub_category varchar(100),
product_name varchar(1000),
sales float,
quantity int,
discount float,
profit float
);
