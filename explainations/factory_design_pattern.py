
from abc import ABC, abstractmethod



# Define the product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass    


# Implemenet concrete product
class Espresso(Coffee):
    def prepare(self):
        return "Espresso is being prepared"

# implement concrete product
class Cappuccino(Coffee):
    def prepare(self):
        return "Cappuccino is being prepared"

class Latte(Coffee):
    def prepare(self):
        return "Latte is being prepared"


class CoffeeMachine:
    
    def make_coffee(self, coffee_type: str):
        if coffee_type == "espresso":
            return Espresso().prepare()
        elif coffee_type == "latte":
            return Latte().prepare()
        elif coffee_type == "cappuccino":
            return Cappuccino().prepare()


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    print(coffee_machine.make_coffee("latte"))

