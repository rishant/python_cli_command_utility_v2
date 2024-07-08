import unittest
from unittest.mock import patch, MagicMock
from app_plugin import AppCliEntryPoint
import json


class TestUserAppCliEntryPoint(unittest.TestCase):

    @patch('utils.mongodb_util.MongoDBUtil.get_client')
    @patch('utils.mongodb_util.MongoDBUtil.get_database')
    @patch('utils.mongodb_util.MongoDBUtil.insert_one')
    @patch('utils.mongodb_util.MongoDBUtil.upsert_one')
    def test_create_user(self, mock_upsert_one, mock_insert_one, mock_get_database, mock_get_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_db = MagicMock()
        mock_get_database.return_value = mock_db
        mock_insert_one.return_value = '668aeef3bb832f5d1fbee458'
        mock_upsert_one.return_value = '668aeef3bb832f5d1fbee458'

        # Create the CLI entry point
        cli = AppCliEntryPoint()

        # Setup test arguments
        args = type('', (), {})()
        args.command = 'create_user'
        args.mongo_uri = 'mongodb://localhost:27017/'
        args.json_data = json.dumps({'user_data': {'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123'}})

        # Execute the CLI command
        result = cli.execute(args)

        # Assert results
        self.assertEqual(result, 'User created with ID: 668aeef3bb832f5d1fbee458')
        mock_get_client.assert_called_once_with('mongodb://localhost:27017/')
        # mock_get_database.assert_called_once_with(mock_client, 'users')
        # mock_insert_one.assert_called_once_with(mock_db, 'user_profiles', {
        #     'username': 'john_doe',
        #     'email': 'john@example.com',
        #     'password': 'password123'
        # })

    @patch('utils.mongodb_util.MongoDBUtil.get_client')
    @patch('utils.mongodb_util.MongoDBUtil.get_database')
    @patch('utils.mongodb_util.MongoDBUtil.find_one')
    def test_get_user(self, mock_find_one, mock_get_database, mock_get_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_db = MagicMock()
        mock_get_database.return_value = mock_db
        userinfo = {'_id': '12345', 'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123'}
        mock_find_one.return_value = userinfo

        # Create the CLI entry point
        cli = AppCliEntryPoint()

        # Setup test arguments
        args = type('', (), {})()
        args.command = 'get_user'
        args.mongo_uri = 'mongodb://localhost:27017/'
        args.json_data = json.dumps({
            'username': 'john_doe'
        })

        # Execute the CLI command
        result = cli.execute(args)

        # Assert results
        self.assertEqual(result, userinfo)
        mock_get_client.assert_called_once_with('mongodb://localhost:27017/')


if __name__ == "__main__":
    unittest.main()
