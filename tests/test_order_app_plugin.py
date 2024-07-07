# tests/test_app_plugin.py
import pytest
from app_plugin import AppCliEntryPoint


def test_create_order():
    cli = AppCliEntryPoint()
    args = type('', (), {})()  # Creating an empty object
    args.command = 'create_order'
    args.json_data = '{"order_id": "123", "item": "book", "quantity": 2}'
    result = cli.execute(args)
    assert result == 'Order created: 123, book, 2'


def test_cancel_order_with_request_body():
    cli = AppCliEntryPoint()
    args = type('', (), {})()
    args.command = 'cancel_order'
    args.json_data = '{"order_id": "123"}'
    result = cli.execute(args)
    assert result == "Order cancelled: {'order_id': '123'}"


def test_status_check():
    cli = AppCliEntryPoint()
    args = type('', (), {})()
    args.command = 'status_check'
    args.json_data = '{}'
    result = cli.execute(args)
    assert result == "Order system status: OK"

