from abc import ABC, abstractmethod


# our Component
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass


# our ConcreteComponents
class PlainCoffee(Coffee):
    def get_cost(self):
        return 1.00

    def get_ingredients(self):
        return "Coffee"


# our base Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_ingredients(self):
        return self._coffee.get_ingredients()


# our ConcreteDecorators
class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 0.25

    def get_ingredients(self):
        return super().get_ingredients() + ", Milk"


class Vanilla(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 0.75

    def get_ingredients(self):
        return super().get_ingredients() + ", Vanilla"


# let's make some coffee!
coffee = PlainCoffee()
print(f"Cost: ${coffee.get_cost()}; Ingredients: {coffee.get_ingredients()}")

coffee = Milk(coffee)
print(f"Cost: ${coffee.get_cost()}; Ingredients: {coffee.get_ingredients()}")

coffee = Vanilla(coffee)
print(f"Cost: ${coffee.get_cost()}; Ingredients: {coffee.get_ingredients()}")
