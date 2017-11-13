# Logs Analysis Project

*Udacity - Full Stack Web Developer Nanodegree*

> A simple command line utility to execute PSQL queries and print the
  response to the three project questions listed below

### basic example
![example](example.gif)
```
$ question 1
```
will produce...
```
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
## Questions

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## How to install
> **NOTE:** *It is assumed that the "news" database has been created
             and the data loaded from newsdata.sql*
### Required packages
- [click](http://click.pocoo.org/6/)
- [psycopg2](https://pypi.python.org/pypi/psycopg2)
- [pygments](http://pygments.org/)
- [tabulate](https://pypi.python.org/pypi/tabulate)

**Before logging into the VM, create a new directory, `news` in the
directory shared with the VM, `vagrant` and clone the repo.**
```
$ git clone https://github.com/klazich/news.git news
```

**Next, login to the VM and move to the new directory news:**
```
$ vagrant ssh
$ cd /vagrant/news
```

**Install the CLI with `pip`:**
```
$ pip install -e .
```

## Usage
`question [--list-only | -l] [--views | -v] [<number>]`

### Command
#### `question`
Takes one argument: 1, 2 or 3 corresponding to the questions listed
above. The printed response is in 4 parts:
  - The question,
  - then the query to be executed,
  - a table with the results,
  - and the status.

### Options
#### `--views`, `-v`
Prints the contents of [views.sql](views.sql) to the console. These are
the views that are created before executing queries.
#### `--list-only`, `-l`
Prints the question and the query and exits before running the query.

### Examples
- To execute the query for question 2, run: `question 2`.
- To see the psql views for this project, run: `question --views`.
- To see what question 3 is and what query will be used but don't want
  to touch the DB, run `question --list-only 3`.
  
## API

### [news.py](news.py)
The CLI entry point. Uses [click](http://click.pocoo.org/6/) to handle the command line interface.

#### `cli(views, number, list-only)`
Handles command line arguments and printing output to `sys.stdout`. Uses the [Interface](interface.py) class to
handle query execution and response.
- **`number`, *str*** - the question number (1, 2 or 3) from `sys.argv`, parsed by [click](http://click.pocoo.org/6/).
- **`views,` *bool*** - an options flag that will print the contents of [views.sql](views.sql) then exit fuction.
- **`list-only`, *bool*** - and options flag to have the function return before initiallizing the DB interface.

### [utils_news.py](utils_news.py)
Utility functions for **news.py**.

#### `QUESTIONS`, *dict*
The three project questions.

#### `QUERY_1`, *str* `QUERY_2`, *str* `QUERY_3`, *str* `QUERYS`, *dict*
The three queries as strings that are executed to answer the questions.

#### `format_query(string)`, *str*
Adds PSQL syntax highlighting to quieries using [pygments](http://pygments.org/).
- **`string`, *str*** - a PSQL query as a string.

#### `format_response(response_obj)`, *str*
Formats the response from [psycopg2](https://pypi.python.org/pypi/psycopg2) after a query is
executed. Uses [tabulate](https://pypi.python.org/pypi/tabulate) to format the returned list
into a more easily readable table.
- **`response_obj` *dict*** - The dictionary returned from the [Interface](interface.py) class.

  Key        | Type   | Value
  -----------|--------|:---------------------------------------------------------------
  `'status'` | *str*  | The status as returned by `curs.statusmessage`.
  `'text'`   | *list* | The list returned by `curs.fetchall()` after a query execution.
  `'query'`  | *str*  | The query returned by `curs.query`.
  `'headers'`| *list* | The table headers parsed from `curs.description`.

### [interface.py](interface.py)
The **Interface** class that handles the DB connection and query execution through 
[psycopg2](https://pypi.python.org/pypi/psycopg2).

#### `DBNAME`, *str*
The name of the the PSQL database.

#### `DB_VIEWS`, *str*
The normalized path to the [views.sql](views.sql) file.

### `Interface`, *interface*
Handles the DB connections through [psycopg2](https://pypi.python.org/pypi/psycopg2).
#### Methods
#### `interface._init_db_views()`
Creates a cursor and executes the [views.sql](views.sql) file, creating the PSQL views needed
for the question queries to work properly. It is called once, when a new instance is created.
#### `interface.execute_query(query)`, *dict*
Creates a cursor and executes a query passed with `query`. Returns a dictionary.
#### `interface.close()`
Closes the connection to the DB.


