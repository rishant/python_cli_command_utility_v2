import argparse
import sys

from app_plugin import AppCliEntryPoint


class Runner:
    def __init__(self):
        self.cli = AppCliEntryPoint()

    def parse_args(self, cli_args):
        parser = argparse.ArgumentParser(description='CLI for router commands')
        parser.add_argument('--command', required=True, help='Command to execute')
        parser.add_argument('--json-data', default='{}', help='JSON data for the command')
        parsed_args = parser.parse_args(cli_args)
        return parsed_args

    def run(self):
        args = self.parse_args(sys.argv[1:])
        result = self.cli.execute(args)
        return result


if __name__ == "__main__":
    runner = Runner()
    result = runner.run()
    print(result)
