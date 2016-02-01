#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import os

import re
import sarge
import yaml
from jinja2 import PackageLoader, Environment

from . import PACKAGE_PATH


def create_file(category, number, overwrite=False):

    filename = "{}_{:03d}.py".format(category, number)
    path = os.path.join(category, filename)

    if os.path.exists(path) and not overwrite:
        print("File already exists.")
        # return

    if not os.path.isdir(category):
        os.makedirs(category)

    problem = get_problem(category, number)

    env = Environment(loader=PackageLoader('challenge_me', 'templates'))
    template = env.get_template("python.template")
    result = template.render(problem=problem, category=category, filename=filename)

    with open(path, "w") as output_file:
        output_file.write(result)


def verify(category, number=None):
    if not number:
        problem_number, filename = get_current_problem(category)
    else:
        problem_number = number
        filename = os.path.join(category, "{:03d}.py".format(number))

    os.chmod(filename, 0o755)

    problem = get_problem(category, problem_number)
    for test in problem["tests"]:
        input_text = str(test["input"])
        output_text = str(test["output"])
        command = sarge.capture_both(filename + " " + input_text)
        if command.stdout.text.strip() != output_text.strip():
            return False, input_text, command.stdout.text.strip(), command.stderr.text.strip(), output_text.strip()

    create_file(category, problem_number + 1)
    return True, None, None, None, None


def get_current_problem(category):
    default = 1, os.path.join(category, "001.py")
    files = glob.glob(category + '/*[0-9][0-9][0-9]*.py')
    if not files:
        create_file(category, 1)
        return default

    filename = max(files)
    number = re.search('.*(\d{3}).*', filename)
    if not number:
        return default

    return int(number.group(1)), filename


def get_problem(category, number):
    with open(os.path.join(PACKAGE_PATH, "challenges", category + ".yaml"), "r") as challenge_file:
        challenges = list(yaml.load_all(challenge_file))

    return challenges[number - 1]


def validate_challenges():
    for entry in glob.glob(PACKAGE_PATH + '/challenges/*.yaml'):
        print(entry)
        with open(entry, "r") as file:
            list(yaml.load_all(file))
