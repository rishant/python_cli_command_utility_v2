# tests/test_app_plugin.py
import pytest
from app_plugin import AppCliEntryPoint


def test_process_payment_with_request_body():
    cli = AppCliEntryPoint()
    args = type('', (), {})()
    args.command = 'process_payment'
    args.json_data = '{"payment_id": "456", "amount": 100.0}'
    result = cli.execute(args)
    assert result == "Payment processed: {'payment_id': '456', 'amount': 100.0}"


def test_refund_payment_with_request_body():
    cli = AppCliEntryPoint()
    args = type('', (), {})()
    args.command = 'refund_payment'
    args.json_data = '{"payment_id": "456"}'
    result = cli.execute(args)
    assert result == "Payment refunded: {'payment_id': '456'}"


def test_process_payment_with_explicit_arguments():
    cli = AppCliEntryPoint()
    args = type('', (), {})()
    args.command = 'process_payment2'
    args.json_data = '{"payment_id": "456", "amount": 100.0}'
    result = cli.execute(args)
    assert result == "Payment processed: 456, 100.0"


def test_refund_payment_with_explicit_argument():
    cli = AppCliEntryPoint()
    args = type('', (), {})()
    args.command = 'refund_payment2'
    args.json_data = '{"payment_id": "456"}'
    result = cli.execute(args)
    assert result == "Payment refunded: 456"
