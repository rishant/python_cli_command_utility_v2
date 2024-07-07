cmd:/> python runner.py --command create_order --json-data "{\"order_id\": \"123\", \"item\": \"book\", \"quantity\": 2}" 
Result:
    Namespace(command='create_order', json_data='{"order_id": "123", "item": "book", "quantity": 2}')

[//]: # (python cli.py --command create_order --json-data '{"order_id": "123", "item": "book", "quantity": 2}')

[//]: # (python cli.py --command cancel_order --json-data '{"order_id": "123"}')

[//]: # (python cli.py --command process_payment --json-data '{"payment_id": "456", "amount": 100.0}')

[//]: # (python cli.py --command refund_payment --json-data '{"payment_id": "456"}')



pytest tests/
