# routers/__init__.py
from .order_router import OrderRouter
from .payment_router import PaymentRouter
from .post_router import PostRouter
from .user_router import UserRouter


# __all__ = ["OrderRouter", "PaymentRouter"]
__all__ = ["OrderRouter", "PaymentRouter", "PostRouter", "UserRouter"]

