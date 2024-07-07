# tests/test_runner_parse_args.py
import unittest
from runner import parse_args


def test_parse_args():
    args = ['--command', 'create_order', '--json-data', '{"order_id": "123", "item": "book", "quantity": 2}']
    parsed_args = parse_args(args)
    assert parsed_args.command == 'create_order'
    assert parsed_args.json_data == '{"order_id": "123", "item": "book", "quantity": 2}'


def test_parse_args_default_json_data():
    args = ['--command', 'create_order']
    parsed_args = parse_args(args)
    assert parsed_args.command == 'create_order'
    assert parsed_args.json_data == '{}'


def test_parse_args_missing_command():
    args = ['--json-data', '{"order_id": "123", "item": "book", "quantity": 2}']
    with unittest.TestCase.assertRaises(unittest.TestCase, SystemExit):
        parse_args(args)
