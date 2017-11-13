#!python3

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
