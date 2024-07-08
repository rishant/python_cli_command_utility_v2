# tests/test_runner_parse_args.py
import unittest
from runner import Runner


class TestRunnerParseArgs(unittest.TestCase):

    def test_parse_args(self):
        args = ['--command', 'odr_create_order', '--json-data', '{"order_id": "123", "item": "book", "quantity": 2}']
        parsed_args = Runner().parse_args(args)
        self.assertEqual(parsed_args.command, 'odr_create_order')
        self.assertEqual(parsed_args.json_data, '{"order_id": "123", "item": "book", "quantity": 2}')

    def test_parse_args_default_json_data(self):
        args = ['--command', 'odr_create_order']
        parsed_args = Runner().parse_args(args)
        self.assertEqual(parsed_args.command, 'odr_create_order')
        self.assertEqual(parsed_args.json_data, '{}')

    def test_parse_args_missing_command(self):
        args = ['--json-data', '{"order_id": "123", "item": "book", "quantity": 2}']
        with self.assertRaises(SystemExit):
            Runner().parse_args(args)


if __name__ == '__main__':
    unittest.main()

