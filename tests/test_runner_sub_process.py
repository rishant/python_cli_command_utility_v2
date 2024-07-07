# test_main_subprocess.py
import subprocess
import json
import os
import pytest

# Determine the directory of the current script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_PY_PATH = os.path.normpath(os.path.join(CURRENT_DIR, '..', 'runner.py'))


@pytest.fixture(autouse=True)
def change_working_directory():
    # Change to the directory where runner.py is located
    os.chdir(CURRENT_DIR)
    yield
    # Optionally revert back to the original directory after each test
    os.chdir(os.path.dirname(CURRENT_DIR))


def test_main_process_payment():
    command = ['python', MAIN_PY_PATH, '--command', 'process_payment', '--json-data',
               '{"payment_id": "456", "amount": 100.0}']
    result = subprocess.run(command, capture_output=True, text=True)

    expected_output = "Payment processed: {'payment_id': '456', 'amount': 100.0}"

    assert result.returncode == 0  # Check if subprocess ran successfully
    assert expected_output in result.stdout.strip()  # Check if expected output is in subprocess stdout


def test_main_status_check():
    command = ['python', MAIN_PY_PATH, '--command', 'status_check']
    result = subprocess.run(command, capture_output=True, text=True)

    expected_output = "Order system status: OK"

    assert result.returncode == 0  # Check if subprocess ran successfully
    assert expected_output in result.stdout.strip()  # Check if expected output is in subprocess stdout


if __name__ == "__main__":
    test_main_process_payment()
    test_main_status_check()
    print("All tests passed successfully!")
