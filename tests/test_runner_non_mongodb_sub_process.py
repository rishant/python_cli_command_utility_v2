# test_main_subprocess.py
import argparse
import unittest
from unittest.mock import patch, MagicMock
import subprocess
import os

from runner import Runner


class TestRunner(unittest.TestCase):
    @patch('runner.AppCliEntryPoint.execute')
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(command='process_payment', json_data='{"payment_id": "456", "amount": 100.0}'))
    def test_run(self, mock_parse_args, mock_execute):
        runner = Runner()
        runner.run()
        mock_execute.assert_called_once_with(argparse.Namespace(command='process_payment', json_data='{"payment_id": "456", "amount": 100.0}'))

    @patch('sys.argv', ['runner.py', '--command', 'process_payment', '--json-data', '{"payment_id": "456", "amount": 100.0}'])
    def test_run_new(self):
        runner = Runner()
        result = runner.run()
        self.assertEqual(result, "Payment processed: {'payment_id': '456', 'amount': 100.0}")


if __name__ == '__main__':
    unittest.main()
