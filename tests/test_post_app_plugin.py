import unittest
from app_plugin import AppCliEntryPoint


class TestUserAppCliEntryPoint(unittest.TestCase):

    def test_posts_v1(self):
        cli = AppCliEntryPoint()
        args = type('', (), {})()
        args.command = 'get_posts'
        args.json_data = '{}'
        result = cli.execute(args)
        assert result is not None

    def test_posts_v2(self):
        cli = AppCliEntryPoint()
        args = type('', (), {})()
        args.command = 'get_external_posts'
        args.api_uri = 'https://jsonplaceholder.typicode.com/posts}'
        args.json_data = '{}'
        result = cli.execute(args)
        assert result is not None


if __name__ == "__main__":
    unittest.main()
