# test_main_subprocess.py
import unittest
from unittest.mock import patch, MagicMock
import subprocess
import os


# Note:
#     1. Testcase broken after integrated MongoDB 'pymongo' with command pattern into router package __init__.py file
#     2. Not able to find a way how to fix that

class TestRunner(unittest.TestCase):

    def setUp(self):
        # Determine the directory of the current script
        CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.runner_path = os.path.normpath(os.path.join(CURRENT_DIR, '..', 'runner.py'))

    def test_main_process_payment(self):
        command = ['python', self.runner_path, '--command', 'process_payment', '--json-data',
                   '{"payment_id": "456", "amount": 100.0}']
        result = subprocess.run(command, capture_output=True, text=True)

        expected_output = "Payment processed: {'payment_id': '456', 'amount': 100.0}"

        assert result.returncode == 0  # Check if subprocess ran successfully
        assert expected_output in result.stdout.strip()  # Check if expected output is in subprocess stdout

    def test_main_status_check(self):
        command = ['python', self.runner_path, '--command', 'status_check']
        result = subprocess.run(command, capture_output=True, text=True)

        expected_output = "Order system status: OK"

        assert result.returncode == 0  # Check if subprocess ran successfully
        assert expected_output in result.stdout.strip()  # Check if expected output is in subprocess stdout


if __name__ == "__main__":
    unittest.main()
    print("All tests passed successfully!")
