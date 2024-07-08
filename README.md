# python client using command design pattern CLI | database | MongoDB | Rest Api | kafka

cmd:/> python runner.py --command odr_create_order --json-data "{\"order_id\": \"123\", \"item\": \"book\", \"quantity\": 2}" 

cmd:/> python runner.py --command odr_create_order --json-data '{"order_id": "123", "item": "book", "quantity": 2}'

cmd:/> python runner.py --command cancel_order --json-data '{"order_id": "123"}'

cmd:/> python runner.py --command process_payment --json-data '{"payment_id": "456", "amount": 100.0}'

cmd:/> python runner.py --command refund_payment --json-data '{"payment_id": "456"}'

cmd:/> python runner.py --command create_user --mongo-uri 'mongodb://localhost:27017/' --json-data '{"username": "john_doe", "email": "john@example.com", "password": "password123"}'

cmd:/> python runner.py --command get_external_posts --api_uri 'https://jsonplaceholder.typicode.com/posts' --json-data '{"username": "john_doe", "email": "john@example.com", "password": "password123"}'


## skip `__pycache__` compiled code generation

    set PYTHONDONTWRITEBYTECODE=1
    python -m unittest discover -s tests


## Create `run_tests.py` script and execute it

    import os
    import unittest
    
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    
    # Discover and run tests
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
