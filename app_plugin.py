# app_plugin.py

import json
import importlib
from inspect import signature

from decorators.command_decorator import command_map

# Ensure all routers are imported here to populate command_map
import routers


class AppCliEntryPoint:
    def __init__(self):
        self.router_modules = {
            'OrderRouter': 'routers.order_router.OrderRouter',
            'PaymentRouter': 'routers.payment_router.PaymentRouter',
            'UserRouter': 'routers.user_router.UserRouter'
        }
        self.routers = {}

    def get_router(self, router_name):
        if router_name not in self.routers:
            if router_name in self.router_modules:
                module_path, class_name = self.router_modules[router_name].rsplit('.', 1)
                module = importlib.import_module(module_path)
                router_class = getattr(module, class_name)
                self.routers[router_name] = router_class()
            else:
                raise ValueError("Unknown router")
        return self.routers[router_name]

    def execute(self, args):

        command = args.command
        json_data = args.json_data

        if command not in command_map:
            raise ValueError("Unknown command")

        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data")

        method = command_map[command]
        router_name = method.__qualname__.split('.')[0]
        router = self.get_router(router_name)

        method_signature = signature(method)
        if len(method_signature.parameters) == 1:
            # Only self is expected
            result = method(router)
        elif len(method_signature.parameters) == 2 and list(method_signature.parameters.values())[1].name == 'request_body':
            # Method expects a request body parameter
            result = method(router, data)
        else:
            # Method expects arbitrary keyword arguments
            result = method(router, **data)

        # print(result)
        return result

