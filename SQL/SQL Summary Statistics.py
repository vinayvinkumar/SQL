## 1. Counting in Python ##

import sqlite3 as sq
conn = sq.connect("factbook.db")
cursor = conn.cursor()
facts = conn.execute("select * from facts;").fetchall()
print(facts)
facts_count = len(facts)

## 2. Counting in SQL ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
ok = cursor.execute("select count(birth_rate) from facts;").fetchall()
birth_rate_count = ok[0][0]
print(birth_rate_count)

## 3. Min and max in SQL ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
min_population_growth = cursor.execute("select min(population_growth) from facts;").fetchall()[0]
print(min_population_growth)
max_death_rate = cursor.execute("select max(death_rate) from facts;").fetchall()[0]
print(max_death_rate)

## 4. Sum and average in SQL ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
total_land_area = cursor.execute("select sum(area_land) from facts;").fetchall()[0]
print(total_land_area)
avg_water_area = cursor.execute("select avg(area_water) from facts;").fetchall()[0]
print(avg_water_area)

## 5. Multiple aggregation functions ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
facts_stats = cursor.execute("select avg(population),sum(population),max(birth_rate) from facts;").fetchall()
print(facts_stats)

## 6. Conditional aggregation ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
population_growth = cursor.execute("select avg(population_growth) from facts where population>10000000;").fetchall()
print(population_growth)

## 7. Selecting unique rows ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
unique_birth_rates = cursor.execute("select distinct birth_rate from facts;").fetchall()
print(unique_birth_rates)

## 8. Distinct aggregations ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
average_birth_rate = cursor.execute("select avg(distinct birth_rate) from facts where population>20000000;").fetchall()[0]
print(average_birth_rate)
sum_population = cursor.execute("select sum(distinct population) from facts where area_land>1000000;").fetchall()[0]
print(sum_population)

## 9. Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
population_growth_millions = cursor.execute("select population_growth/1000000.0 from facts;").fetchall()
print(population_growth_millions)

## 10. Arithmetic between columns ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
next_year_population = cursor.execute("select (population*population_growth)+population from facts;").fetchall()
print(next_year_population)