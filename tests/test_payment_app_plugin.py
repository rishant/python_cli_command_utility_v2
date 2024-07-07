# tests/test_app_plugin.py
import unittest
from app_plugin import AppCliEntryPoint


class TestPaymentAppCliEntryPoint(unittest.TestCase):

    def test_process_payment_with_request_body(self):
        cli = AppCliEntryPoint()
        args = type('', (), {})()
        args.command = 'process_payment'
        args.json_data = '{"payment_id": "456", "amount": 100.0}'
        result = cli.execute(args)
        assert result == "Payment processed: {'payment_id': '456', 'amount': 100.0}"

    def test_refund_payment_with_request_body(self):
        cli = AppCliEntryPoint()
        args = type('', (), {})()
        args.command = 'refund_payment'
        args.json_data = '{"payment_id": "456"}'
        result = cli.execute(args)
        assert result == "Payment refunded: {'payment_id': '456'}"

    def test_process_payment_with_explicit_arguments(self):
        cli = AppCliEntryPoint()
        args = type('', (), {})()
        args.command = 'process_payment2'
        args.json_data = '{"payment_id": "456", "amount": 100.0}'
        result = cli.execute(args)
        assert result == "Payment processed: 456, 100.0"

    def test_refund_payment_with_explicit_argument(self):
        cli = AppCliEntryPoint()
        args = type('', (), {})()
        args.command = 'refund_payment2'
        args.json_data = '{"payment_id": "456"}'
        result = cli.execute(args)
        assert result == "Payment refunded: 456"


if __name__ == "__main__":
    unittest.main()

