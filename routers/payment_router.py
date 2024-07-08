# routers/payment_router.py
from decorators.command_decorator import command


class PaymentRouter:
    @command('process_payment')
    def process_payment(self, request_body):
        return f"Payment processed: {request_body}"

    @command('refund_payment')
    def refund_payment(self, request_body):
        return f"Payment refunded: {request_body}"

    @command('process_payment2')
    def process_payment(self, request_body):
        return f"Payment processed: {request_body['payment_id']}, {request_body['amount']}"

    @command('refund_payment2')
    def refund_payment(self, request_body):
        return f"Payment refunded: {request_body['payment_id']}"

