
from abc import ABC, abstractmethod


# Define the Strategy Interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Define the concrete Strategies:

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using creditcard."

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using paypal."

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using bitcoin."


# Define the context:
class ShippingCart:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def checkout(self, amount):
        return self.payment_method.pay(amount)


if __name__ == "__main__":
    ship_obj = ShippingCart(CreditCardPayment())
    print(ship_obj.checkout(100))


