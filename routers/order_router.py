# routers/order_router.py
from decorators.command_decorator import command


class OrderRouter:
    @command('odr_create_order')
    def create_order(self, json_data):
        return f"Order created: {json_data['order_id']}, {json_data['item']}, {json_data['quantity']}"

    @command('cancel_order')
    def cancel_order(self, json_data):
        return f"Order cancelled: {json_data}"

    @command('status_check')
    def status_check(self):
        return "Order system status: OK"

