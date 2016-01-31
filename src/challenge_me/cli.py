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

from challenge_me import challenge_me


@click.group()
def main():
    pass


@main.command()
@click.argument('category')
def start(category):
    """
    Starting a challenge.

    Args:
        category:
    """
    click.echo('Starting a challenge.')
    challenge_me.create_file(category, 1)


@main.command()
@click.argument('category')
def verify(category):
    """
    Verifying a challenge.
    :param category:
    """
    click.echo('Verifying a challenge.')

    success, input_text, result, error, expected = challenge_me.verify(category)
    if success:
        click.echo('Success.')
    elif error:
        click.echo('Failure.')
        click.echo('Error: {}'.format(error))
    else:
        click.echo('Failure.')
        click.echo('Input: {}'.format(input_text))
        click.echo('Result: {}'.format(result))
        click.echo('Expected: {}'.format(expected))


@main.command()
def skip():
    """
    Skipping a challenge.
    """
    click.echo('Skipping a challenge.')


@main.command()
def test():
    """
    Testing functionality
    """
    click.echo('Testing.')
    challenge_me.verify("string")


if __name__ == "__main__":
    main()
