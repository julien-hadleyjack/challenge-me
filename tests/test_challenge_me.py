import glob
import unittest

import yaml
from click.testing import CliRunner

from challenge_me import PACKAGE_PATH
from challenge_me.cli import main


class TestEpisode(unittest.TestCase):

    def test_main(self):
        runner = CliRunner()
        result = runner.invoke(main, ["--version"])

        self.assertIn("challenge-me", result.output)
        self.assertEqual(result.exit_code, 0)

    def test_yaml(self):
        for entry in glob.glob(PACKAGE_PATH + '/challenges/*.yaml'):
            with open(entry, "r") as file:
                list(yaml.load_all(file))
