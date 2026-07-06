from abc import ABC, abstractmethod
from app.user import User

class Payment(ABC):
    @abstractmethod
    def process_payment(self, user: User, amount: float):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, user: User, amount: float):
        # Logic to process credit card payment
        print(f"Processing credit card payment of ${amount} for user {user.get_username()}")
    

class PayPalPayment(Payment):
    def process_payment(self, user: User, amount: float):
        # Logic to process PayPal payment
        print(f"Processing PayPal payment of ${amount} for user {user.get_username()}")
