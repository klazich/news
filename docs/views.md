*Views can be found in the [views.sql](https://github.com/klazich/news/views.sql) file.*

## path_hits
Counts sucessful hits to paths in the `log` table. Used by `top_articles`.
```sql
CREATE VIEW path_hits AS
  SELECT
    count(*) AS hits,
    path
  FROM log
  WHERE status = '200 OK' AND NOT path = '/'
  GROUP BY path;
```

## top_articles
Joins the `articles` table with `path_hits` view to show articles with most hits. Used in queries for question 1 and 2.
```sql
CREATE VIEW top_articles AS
  SELECT
    articles.title,
    path_hits.hits,
    articles.author
  FROM articles, path_hits
  WHERE path_hits.path = concat('/article/', articles.slug)
  ORDER BY hits DESC;
```

## daily_404
Counts failed requests for each day in the `log` table. Used in `daily_stats`.
```sql
CREATE VIEW daily_404 AS
  SELECT
    date(time) AS day,
    count(*)   AS not_found
  FROM log
  WHERE status = '404 NOT FOUND'
  GROUP BY day;
```

## daily_requests
Counts request attempts for each day in the `log` table. Used in `daily_stats`.
```sql
CREATE VIEW daily_requests AS
  SELECT
    date(time) AS day,
    count(*)   AS requests
  FROM log
  GROUP BY day;
```

## daily_stats
Joins the views `daily_404` and `daily_requests` to show failed requests as a percentage. Used in the query to answer question 2.
```sql
CREATE VIEW daily_stats AS
  SELECT
    daily_requests.day,
    requests,
    not_found,
    ROUND(100.0 * not_found / requests, 2) AS percent
  FROM daily_404, daily_requests
  WHERE daily_404.day = daily_requests.day;
```