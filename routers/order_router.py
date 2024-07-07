# routers/order_router.py
from decorators.command_decorator import command


class OrderRouter:
    @command('create_order')
    def create_order(self, order_id, item, quantity):
        return f"Order created: {order_id}, {item}, {quantity}"

    @command('cancel_order')
    def cancel_order(self, request_body):
        return f"Order cancelled: {request_body}"

    @command('status_check')
    def status_check(self):
        return "Order system status: OK"