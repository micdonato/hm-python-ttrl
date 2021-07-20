# src/hypermodern_python/console.py

# imports are split in blocks: standard libraries
import textwrap

# third party packages
import click
import requests

# local imports
from . import __version__, wikipedia

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version=__version__)
def main():
    """The hm Python tutorial."""
    data = wikipedia.random_page()

    title = data['title']
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
