## Question 1
```
vagrant@vagrant:/vagrant/news$ question 1

1. What are the most popular three articles of all time?

    SELECT
      title,
      hits
    FROM top_articles
    LIMIT 3;

 title                            |   hits
----------------------------------+--------
 Candidate is jerk, alleges rival | 338647
 Bears love berries, alleges bear | 253801
 Bad things gone, say good people | 170098

 SELECT 3
```

## Question 2
```
vagrant@vagrant:/vagrant/news$ question 2

2. Who are the most popular article authors of all time?

    SELECT
      name,
      sum(hits) AS views
    FROM authors, top_articles
    WHERE authors.id = author
    GROUP BY name
    ORDER BY views DESC;

 name                   |   views
------------------------+---------
 Ursula La Multa        |  507594
 Rudolf von Treppenwitz |  423457
 Anonymous Contributor  |  170098
 Markoff Chaney         |   84557

 SELECT 4
```

## Question 3
```
vagrant@vagrant:/vagrant/news$ question 3

3. On which days did more than 1% of requests lead to errors?

    SELECT *
    FROM daily_stats
    WHERE percent >= 1
    ORDER BY percent DESC;

 day        |   requests |   not_found |   percent
------------+------------+-------------+-----------
 2016-07-17 |      55907 |        1265 |      2.26

 SELECT 1
```