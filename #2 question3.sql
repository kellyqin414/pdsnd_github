WITH t1 AS (SELECT customer_id customer_id1, SUM(amount)
            FROM payment
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT 10),
     t2 AS (SELECT customer_id, SUM(amount) payment, DATE_TRUNC('month', payment_date) date_month, COUNT(payment) payment_count
FROM payment
JOIN t1
ON payment.customer_id=t1.customer_id1
GROUP BY 1, 3)
SELECT CONCAT(c.first_name, ' ' ,c.last_name) full_name, t2.date_month, t2.payment_count, t2.payment payment_amount, 
LAG(t2.payment) OVER(PARTITION BY CONCAT(c.first_name, ' ' ,c.last_name) ORDER BY t2.date_month ), 
t2.payment - LAG(t2.payment) OVER(PARTITION BY CONCAT(c.first_name, ' ' ,c.last_name) ORDER BY t2.date_month ) difference
FROM t2
JOIN customer c
ON t2.customer_id=c.customer_id
ORDER BY difference
