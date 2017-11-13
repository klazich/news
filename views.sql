DROP VIEW IF EXISTS path_hits, top_articles, daily_404, daily_requests, daily_stats;

CREATE VIEW path_hits AS
  SELECT
    count(*) AS hits,
    path
  FROM log
  WHERE status = '200 OK' AND NOT path = '/'
  GROUP BY path;

CREATE VIEW top_articles AS
  SELECT
    articles.title,
    path_hits.hits,
    articles.author
  FROM articles, path_hits
  WHERE path_hits.path = concat('/article/', articles.slug)
  ORDER BY hits DESC;

CREATE VIEW daily_404 AS
  SELECT
    date(time) AS day,
    count(*)   AS not_found
  FROM log
  WHERE status = '404 NOT FOUND'
  GROUP BY day;

CREATE VIEW daily_requests AS
  SELECT
    date(time) AS day,
    count(*)   AS requests
  FROM log
  GROUP BY day;

CREATE VIEW daily_stats AS
  SELECT
    daily_requests.day,
    requests,
    not_found,
    ROUND(100.0 * not_found / requests, 2) AS percent
  FROM daily_404, daily_requests
  WHERE daily_404.day = daily_requests.day;
