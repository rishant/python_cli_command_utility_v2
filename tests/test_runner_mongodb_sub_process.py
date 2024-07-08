import unittest
from unittest.mock import patch, MagicMock
import subprocess
import json
import sys
import os


class TestRunner(unittest.TestCase):

    # test_create_user - Working
    @patch('utils.mongodb_util.MongoDBUtil.get_client')
    @patch('utils.mongodb_util.MongoDBUtil.get_database')
    @patch('utils.mongodb_util.MongoDBUtil.insert_one')
    @patch('utils.mongodb_util.MongoDBUtil.upsert_one')
    def test_create_user(self, mock_upsert_one, mock_insert_one, mock_get_database, mock_get_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_database = MagicMock()
        mock_get_database.return_value = mock_database
        mock_insert_one.return_value = '668aeef3bb832f5d1fbee458'
        mock_upsert_one.return_value = '668aeef3bb832f5d1fbee458'

        # Define the command and JSON data
        command = 'create_user'
        mongo_uri = 'mongodb://localhost:27017/'
        json_data = json.dumps({
                # '_id': '668aeef3bb832f5d1fbee458',
                'username': 'john_doe',
                'email': 'john@example.com',
                'password': 'password123'
        })

        # Run the runner.py script using subprocess
        result = subprocess.run(
            [sys.executable, '../runner.py', '--command', command, '--mongo-uri', mongo_uri, '--json-data', json_data],
            capture_output=True,
            text=True
        )

        # Check if the insert_one method was called with the expected arguments
        # mock_insert_one.assert_called_once_with(mock_database, 'user_profiles', {
        #     'username': 'john_doe',
        #     'email': 'john@example.com',
        #     'password': 'password123'
        # })

        # Check if the upsert_one method was called with the expected arguments
        # mock_upsert_one.assert_called_once_with(mock_database, 'user_profiles', {
        #     '_id': '668aeef3bb832f5d1fbee458',
        #     'username': 'john_doe',
        #     'email': 'john@example.com',
        #     'password': 'password123'
        # })

        # Check the result
        self.assertIn("User created with ID: ", result.stdout)
        # mock_insert_one.assert_called_once()

    # test_get_user_by_id - Working
    @patch('utils.mongodb_util.MongoDBUtil.get_client')
    @patch('utils.mongodb_util.MongoDBUtil.get_database')
    @patch('utils.mongodb_util.MongoDBUtil.find_one')
    def test_get_user_by_id(self, mock_find_one, mock_get_database, mock_get_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_database = MagicMock()
        mock_get_database.return_value = mock_database
        mock_find_one.return_value = {'_id': '668aeef3bb832f5d1fbee458', 'username': 'john_doe',
                                      'email': 'john@example.com'}

        # Define the command and JSON data
        command = 'get_user_by_id'
        json_data = json.dumps({
            'mongo_uri': 'mongodb://localhost:27017/',
            'user_id': '668aeef3bb832f5d1fbee458'
        })

        # Run the runner.py script using subprocess
        result = subprocess.run(
            [sys.executable, '../runner.py', '--command', command, '--json-data', json_data],
            capture_output=True,
            text=True
        )

        # Check if the find_one method was called with the expected arguments
        # mock_find_one.assert_called_once()
        self.assertIn('"username": "john_doe"', result.stdout)

    @patch('utils.mongodb_util.MongoDBUtil.get_client')
    @patch('utils.mongodb_util.MongoDBUtil.get_database')
    @patch('utils.mongodb_util.MongoDBUtil.find_one')
    @patch('utils.mongodb_util.MongoDBUtil.update_one')
    def test_update_user(self, mock_update_one, mock_find_one, mock_get_database, mock_get_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_database = MagicMock()
        mock_get_database.return_value = mock_database
        mock_update_one.return_value = 1

        # Define the command and JSON data
        command = 'update_user'
        json_data = json.dumps({
            'mongo_uri': 'mongodb://localhost:27017/',
            'user_id': '668aeef3bb832f5d1fbee458',
            'update_data': {
                'email': 'john_new@example.com'
            }
        })

        # Run the runner.py script using subprocess
        result = subprocess.run(
            [sys.executable, 'runner.py', '--command', command, '--json-data', json_data],
            capture_output=True,
            text=True
        )

        # Check if the update_one method was called with the expected arguments
        mock_update_one.assert_called_once()
        self.assertIn("User with ID 12345 updated successfully", result.stdout)

    @patch('utils.mongodb_util.MongoDBUtil.get_client')
    @patch('utils.mongodb_util.MongoDBUtil.get_database')
    @patch('utils.mongodb_util.MongoDBUtil.delete_one')
    def test_delete_user(self, mock_delete_one, mock_find_one, mock_get_database, mock_get_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_database = MagicMock()
        mock_get_database.return_value = mock_database
        mock_delete_one.return_value = 1

        # Define the command and JSON data
        command = 'delete_user'
        json_data = json.dumps({
            'mongo_uri': 'mongodb://localhost:27017/',
            'user_id': '668aeef3bb832f5d1fbee458'
        })

        # Run the runner.py script using subprocess
        result = subprocess.run(
            [sys.executable, 'runner.py', '--command', command, '--json-data', json_data],
            capture_output=True,
            text=True
        )

        # Check if the delete_one method was called with the expected arguments
        mock_delete_one.assert_called_once()
        self.assertIn("User with ID 668aeef3bb832f5d1fbee458 deleted successfully", result.stdout)


if __name__ == "__main__":
    unittest.main()
    print("All tests passed successfully!")
