import argparse
import sys

from app_plugin import AppCliEntryPoint


def parse_args(cli_args):
    parser = argparse.ArgumentParser(description='CLI for router commands')
    parser.add_argument('--command', required=True, help='Command to execute')
    parser.add_argument('--json-data', default='{}', help='JSON data for the command')
    parsed_args = parser.parse_args(cli_args)
    return parsed_args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    # print(args)

    cli = AppCliEntryPoint()
    result = cli.execute(args)
    print(result)
