# test_main_subprocess.py
import argparse
import unittest
from unittest.mock import patch

from runner import Runner


class TestRunner(unittest.TestCase):
    @patch('runner.AppCliEntryPoint.execute')
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(command='get_posts'))
    def test_run(self, mock_parse_args, mock_execute):
        runner = Runner()
        runner.run()
        mock_execute.assert_called_once_with(argparse.Namespace(command='get_posts'))

    @patch('sys.argv', ['runner.py', '--command', 'get_posts'])
    def test_run_new(self):
        runner = Runner()
        result = runner.run()
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
