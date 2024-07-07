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
    def process_payment(self, payment_id, amount):
        return f"Payment processed: {payment_id}, {amount}"

    @command('refund_payment2')
    def refund_payment(self, payment_id):
        return f"Payment refunded: {payment_id}"

