"""FSND Logs Analysis Project

Here are the questions the reporting tool should answer:

1. What are the most popular three articles of all time?

    Which articles have been accessed the most? Present this information as a
    sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time?

    That is, when you sum up all of the articles each author has written, which
    authors get the most page views? Present this as a sorted list with
    the most popular author at the top.

3. On which days did more than 1% of requests lead to errors?

    The log table includes a column status that indicates the HTTP status code
    that the news site sent to the user's browser.
"""
from os import path

import click

import utils_news
import interface


@click.command(name='news')
@click.option('--views', '-v', is_flag=True, help='list psql views')
@click.option('--list-only', '-l', is_flag=True, help='list question and query without executing')
@click.argument('number', required=False)
def cli(views, number, list_only):
    """A simple CLI to answer project questions."""

    if views:
        file_path = path.normpath('/vagrant/news/views.sql')
        with open(file_path, 'r') as f:
            click.echo(utils_news.format_query(f.read()))
        return

    if number not in ['1', '2', '3']:
        err = click.UsageError('question number must be 1, 2 or 3')
        raise err

    question = utils_news.QUESTIONS[number]
    query = utils_news.QUERIES[number]

    click.echo('')
    click.secho(question, bold=True, fg='yellow')
    click.echo('')
    click.echo(utils_news.format_query(query))

    # if "list-only" option is passed than exit
    if list_only:
        return

    db_io = interface.Interface()

    response = db_io.execute_query(query)
    click.echo(utils_news.format_response(response))
    click.echo('')

    db_io.close()
