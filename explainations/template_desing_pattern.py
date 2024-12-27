from abc import ABC, abstractmethod
import os


# Define Abstarct Class 
class DiningExperiance(ABC):

    # template method define the skeleton of dining exp.
    def serve_dineer(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()

    @abstractmethod
    def serve_appetizer(self):
        pass

    @abstractmethod
    def serve_main_course(self):
        pass

    @abstractmethod
    def serve_dessert(self):
        pass

    @abstractmethod
    def serve_beverage(self):
        pass


# Define Concrete Class1
class IndianFood(DiningExperiance):

    def serve_appetizer(self):
        print("Serving Papadum")

    def serve_main_course(self):
        print("Serving Chicken Tikka Masala")
    
    def serve_dessert(self):
        print("Serving Gulab Jamun")
    
    def serve_beverage(self):
        print("Serving Mango Lassi")


# Define Concrete Class 2:
class ChainesFood(DiningExperiance):
    def serve_appetizer(self):
        print("Serving Onion Rings")
    
    def serve_main_course(self):
        print("Serving Steak")

    def serve_dessert(self):
        print("Serving Cheesecake")

    def serve_beverage(self):
        print("Serving Iced Tea")


if __name__ == "__main__":

    obj=IndianFood()
    obj.serve_dineer()
    print('\n -------Change------')
    obj=ChainesFood()
    obj.serve_dineer()
    