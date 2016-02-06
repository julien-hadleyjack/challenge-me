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
import glob

import click

from . import challenge_me, __version__


@click.group()
@click.version_option(prog_name="challenge-me", version=__version__)
def main():
    pass


@main.command()
@click.argument('category', required=False)
@click.option('--language', default="python", required=False)
def start(category, language):
    """
    Starting a challenge.

    Args:
        language:
        category:
    """

    if not category:
        category, number, filename = challenge_me.get_current_challenge()
        if not category:
            click.echo("Couldn't find a category with open challenges. Stopping.")
            return

        if number != 1:
            click.echo("File(s) already exist for this category. Skipped creating new one.")
            return

    challenge = challenge_me.get_challenge_with_test(category, 1)
    if challenge is None:
        click.echo("Couldn't find a challenge to use. Stopping.")
        return

    click.echo('Starting first challenge for category {}.'.format(category))
    try:
        challenge_me.create_file(challenge, language)
    except ValueError as e:
        click.echo(str(e) + " Stopping.")


@main.command()
@click.argument('category', required=False)
@click.argument('number', required=False)
@click.option('--language', default="python", required=False)
def verify(category, number, language):
    """
    Verifying a challenge.

    Args:
        language:
        number:
        category:
    """

    if not category or not number:
        new_category, new_number, _ = challenge_me.get_current_challenge()

        if not category:
            category = new_category

        if not number:
            number = new_number

    search = glob.glob(category + "/*{:03d}*.py".format(number))
    if not search:
        click.echo("Couldn't find file to verify")
        return 1, None
    else:
        filename = search[0]

    challenge = challenge_me.get_challenge(category, number)

    click.echo('Verifying challenge {} for category {}.'.format(number, category))
    success, input_text, output_text, command = challenge_me.verify(challenge, filename)
    if success:
        click.secho("Success.", fg='green')
        click.echo("Creating file for next challenge.")
        new_challenge = challenge_me.get_challenge_with_test(category, number + 1)
        challenge_me.create_file(new_challenge, language)

    else:
        click.secho('Failure.', fg='red')
        click.echo('Input: {}'.format(input_text))
        click.echo('Result: {}'.format(command.stdout.text.strip()))
        click.echo('Expected: {}'.format(output_text.strip()))

    if command.stderr.text:
        click.echo('Error: {}'.format(command.stderr.text))


@main.command()
@click.argument('category', required=False)
@click.option('--language', default="python", required=False)
def skip(category, language):
    """
    Skipping a challenge.

    Args:
        language:
        category:
    """
    click.echo('Skipping a challenge.')

    if not category:
        category, number = challenge_me.get_current_challenge()
        click.echo('Problem {} in category {} was selected.'.format(number, category))

    number, filename = challenge_me.get_current_attempt_in_category(category)
    new_challenge = challenge_me.get_challenge_with_test(category, number + 1)
    challenge_me.create_file(new_challenge, language)


@main.command()
def test():
    """
    Testing functionality
    """
    click.echo('Testing.')


if __name__ == "__main__":
    main()
