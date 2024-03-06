from abc import ABC, abstractmethod


class IBuilder(ABC):

    @abstractmethod
    def set_num_stories(self):
        pass

    @abstractmethod
    def set_door_type(self):
        pass

    @abstractmethod
    def set_roof_type(self):
        pass


# concrete builder class

class ConcreteBuilder(IBuilder):

    def __init__(self):
        self.house = House()

    def set_door_type(self):
        self.house.add("Single")

    def set_roof_type(self):
        self.house.add("slenting")

    def set_num_stories(self):
        self.house.add("5")


class House:
    """
      It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    """

    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def list_parts(self):
        print(f"House has {','.join(self._parts)}")


class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_house(self):
        self._builder.set_num_stories()
        self._builder.set_roof_type()
        self._builder.set_door_type()
        return self._builder.house
