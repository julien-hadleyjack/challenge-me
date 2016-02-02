#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mchallenge_me` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``challenge_me.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``challenge_me.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click

from . import challenge_me, __version__


@click.group()
@click.version_option(prog_name="challenge-me", version=__version__)
def main():
    pass


@main.command()
@click.argument('category', required=False)
def start(category):
    """
    Starting a challenge.

    Args:
        category:
    """
    click.echo('Starting a challenge.')

    if not category:
        category, number = challenge_me.get_global_problem()
        click.echo('Problem {} in category {} was selected.'.format(number, category))

    challenge_me.create_file(category, 1)


@main.command()
@click.argument('category', required=False)
def verify(category):
    """
    Verifying a challenge.

    Args:
        category:
    """
    click.echo('Verifying a challenge.')

    if not category:
        category, number = challenge_me.get_global_problem()
        click.echo('Problem {} in category {} was selected.'.format(number, category))

    success, input_text, result, error, expected = challenge_me.verify(category)
    if success:
        click.echo('Success.')
    else:
        click.echo('Failure.')
        click.echo('Input: {}'.format(input_text))
        click.echo('Result: {}'.format(result))
        click.echo('Expected: {}'.format(expected))

    if error:
        click.echo('Error: {}'.format(error))


@main.command()
@click.argument('category', required=False)
def skip(category):
    """
    Skipping a challenge.

    Args:
        category:
    """
    click.echo('Skipping a challenge.')

    if not category:
        category, number = challenge_me.get_global_problem()
        click.echo('Problem {} in category {} was selected.'.format(number, category))

    number, filename = challenge_me.get_current_problem(category)
    challenge_me.create_file(category, number + 1)


@main.command()
def test():
    """
    Testing functionality
    """
    click.echo('Testing.')


if __name__ == "__main__":
    main()
