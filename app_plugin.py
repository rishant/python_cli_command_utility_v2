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
            'UserRouter': 'routers.user_router.UserRouter',
            'PostRouter': 'routers.post_router.PostRouter'
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

    def parse_and_merge_json_data(self, args):
        if hasattr(args, 'json_data'):
            try:
                args.json_data = json.loads(args.json_data)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON data")

        additional_args = vars(args).copy()
        return additional_args

    def determine_method_call(self, method, router, json_data):
        method_signature = signature(method)
        json_param_names = {'json_data', 'json_request', 'json_args', 'request_body'}

        if len(method_signature.parameters) == 1:
            return method(router)
        else:
            params = list(method_signature.parameters.values())
            if len(params) == 2 and params[1].name in json_param_names:
                return method(router, json_data['json_data'])
            else:
                kwargs = {param: json_data[param] for param in method_signature.parameters if param in json_data}
                return method(router, **kwargs)

    def execute(self, args):
        command = args.command

        if command not in command_map:
            raise ValueError("Unknown command")

        json_data = self.parse_and_merge_json_data(args)
        method = command_map[command]
        router_name = method.__qualname__.split('.')[0]
        router = self.get_router(router_name)
        result = self.determine_method_call(method, router, json_data)

        return result

