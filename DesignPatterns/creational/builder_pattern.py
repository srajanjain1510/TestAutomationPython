from abc import ABC, abstractmethod


class IBuilder(ABC):

    @staticmethod
    @abstractmethod
    def set_num_stories(self, value):
        pass

    @staticmethod
    @abstractmethod
    def set_door_type(self, value):
        pass

    @staticmethod
    @abstractmethod
    def set_roof_type(self, value):
        pass


# concrete builder class

class ConcreteBuilder(IBuilder):

    def __init__(self):
        self.house = House()

    def set_door_type(self, value):
        self.house.set_door_type(value)

    def set_roof_type(self, value):
        self.house.set_roof_type(value)

    def set_num_stories(self, value):
        self.house.set_num_stories(value)

    def build_house(self):
        return self.house


class House:
    """
      It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    """

    def __init__(self):
        self.num_stories = None
        self.door_type = None
        self.roof_type = None

    def set_door_type(self, value):
        self.door_type = value

    def set_roof_type(self, value):
        self.roof_type = value

    def set_num_stories(self, value):
        self.num_stories = value

    def __str__(self):
        return f"This is customized house with {self.door_type} , {self.roof_type} and {self.num_stories}"


class Director:
    def __init__(self):
        self._builder = IBuilder

    def set_builder(self,builder):
        self._builder = builder

    def construct(self):

        house = House()
        self._builder.set_roof_type(house.roof_type)
        self._builder.set_door_type(house.door_type)
        self._builder.set_num_stories(house.num_stories)

        return house

