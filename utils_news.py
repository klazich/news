from pygments import highlight
from pygments.lexers.sql import PostgresLexer
from pygments.formatters import TerminalFormatter, TerminalTrueColorFormatter
from tabulate import tabulate

QUESTIONS = {'1': '1. What are the most popular three articles of all time?',
             '2': '2. Who are the most popular article authors of all time?',
             '3': '3. On which days did more than 1% of requests lead to errors?'}

QUERY_1 = """SELECT
  title,
  hits
FROM top_articles
LIMIT 3;"""

QUERY_2 = """SELECT
  name,
  sum(hits) AS views
FROM authors, top_articles
WHERE authors.id = author
GROUP BY name
ORDER BY views DESC;"""

QUERY_3 = """SELECT *
FROM daily_stats
WHERE percent >= 1
ORDER BY percent DESC;"""

QUERIES = {'1': QUERY_1,
           '2': QUERY_2,
           '3': QUERY_3}


def format_query(string):
    """psql syntax highlighting for printing queries."""
    string_list = string.split('\n')
    code = '\n'.join('    ' + line for line in string_list)
    return highlight(code, PostgresLexer(), TerminalTrueColorFormatter())


def format_response(response_obj):
    """format query response for console output."""
    headers = response_obj['headers']
    table = response_obj['text']
    status = response_obj['status']
    return tabulate(table, headers=headers, tablefmt='presto') + '\n\n ' + status
