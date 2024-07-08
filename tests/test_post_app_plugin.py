import unittest
from app_plugin import AppCliEntryPoint


class TestUserAppCliEntryPoint(unittest.TestCase):

    def test_status_check(self):
        cli = AppCliEntryPoint()
        args = type('', (), {})()
        args.command = 'get_posts'
        args.json_data = '{}'
        result = cli.execute(args)
        assert result is not None


if __name__ == "__main__":
    unittest.main()
