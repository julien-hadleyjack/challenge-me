#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import os

import re
import sarge
import yaml
from jinja2 import PackageLoader, Environment

from . import PACKAGE_PATH


FILENAME_TEMPLATE = {
    "python": "{category}_{number:03d}.py"
}


def create_file(challenge, language, overwrite=False):
    category = challenge["category"]
    number = challenge["number"]

    file_name = FILENAME_TEMPLATE.get(language).format(category=category, number=number)
    file_path = os.path.join(category, file_name)

    if os.path.exists(file_path) and not overwrite:
        raise ValueError("A file for this challenge was already created.")

    if not os.path.isdir(category):
        os.makedirs(category)

    env = Environment(loader=PackageLoader('challenge_me', 'templates'))
    template = env.get_template(language + ".template")
    result = template.render(challenge=challenge, category=category, filename=file_name)

    with open(file_path, "w") as output_file:
        output_file.write(result)


def verify(challenge, filename):

    os.chmod(filename, 0o755)

    for test in challenge["tests"]:
        input_text = str(test["input"])
        output_text = str(test["output"])
        command = sarge.capture_both(filename + " " + input_text)
        if command.stdout.text.strip() != output_text.strip():
            return False, input_text, output_text, command

    return True, None, None, None


def get_current_attempt_in_category(category=None):
    files = glob.glob(category + '/*[0-9][0-9][0-9]*.*')
    if not files:
        return 1, None

    filename = max(files)
    number = re.search('.*(\d{3}).*', filename)
    if not number:
        return 1, None

    return int(number.group(1)), filename


def get_challenge(category, number):
    file_name = os.path.join(PACKAGE_PATH, "challenges", category + ".yaml")
    with open(file_name, "r") as challenge_file:
        challenges = list(yaml.load_all(challenge_file))

    if number - 1 < len(challenges):
        challenge = challenges[number - 1]
        challenge["category"] = category
        challenge["number"] = number
        return challenge
    else:
        return None


def get_current_challenge():
    file_path = os.path.join(PACKAGE_PATH, "challenges")
    for filename in glob.glob(file_path + '/*.yaml'):
        category = re.search('.*/(.+)\.yaml', filename)
        if not category:
            continue
        category = category.group(1)

        with open(filename, "r") as challenge_file:
            number, filename = get_current_attempt_in_category(category)

            if number <= len(list(yaml.load_all(challenge_file))):
                return category, number, filename

    return None, -1, None


def get_challenge_with_test(category, number):
    challenge = get_challenge(category, number)
    while challenge is not None and "tests" not in challenge:
        number += 1
        challenge = get_challenge(category, number)
    return challenge
