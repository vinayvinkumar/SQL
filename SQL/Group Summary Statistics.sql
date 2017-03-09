## 1. Statistics by group ##

select * from recent_grads limit 5

## 2. The GROUP BY statement ##

SELECT Major_category, AVG(ShareWomen) FROM recent_grads GROUP BY Major_category;

## 3. The AS statement ##

select sum(men) as total_men,sum(women) as total_women from recent_grads;

## 4. Practice: Using GROUP BY ##

select Major_category,avg(employed)/avg(total) as share_employed from recent_grads group by Major_category;

## 5. The HAVING statement ##

select Major_category,avg(Low_wage_jobs)/avg(Total) as share_low_wage from recent_grads group by Major_category having share_low_wage > 0.1;

## 6. The ROUND function ##

SELECT ROUND(ShareWomen, 4), Major_category FROM recent_grads LIMIT 10;

## 7. Nested functions ##

select Major_category,round(avg(College_jobs)/avg(Total),3) as share_degree_jobs from recent_grads group by Major_category having share_degree_jobs < 0.3;