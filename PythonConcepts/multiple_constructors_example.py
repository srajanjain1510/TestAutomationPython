from functools import singledispatchmethod


class RequestPayload:

    def __init__(self, *args):
        if len(args) > 0:
            self.name, self.age, self.email = args[0], args[1], args[2]

    def __str__(self):
        return f"all arguments are name={self.name} age = {self.age} and email={self.email}"


obj_payload = RequestPayload('sj', 35, 'sj@gmail.com')
print(obj_payload)


# using class method Multiple constructors

class DateCalculation:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"data is {self.data}"

    @classmethod
    def from_list(cls, data_list):
        return cls(data_list)

    @classmethod
    def from_string(cls, data_str):
        return cls(data_str)


object_date_calculation = DateCalculation.from_list([1, 2, 3])
print(object_date_calculation)
obj2 = DateCalculation.from_string('srtgrgr')
print(obj2)


# multiple constructor using @singlemethoddispatch

class Sample:

    def __init__(self, data):
        self.data_source = data

    def __str__(self):
        return f"Data is {self.data_source}"

    @singledispatchmethod
    def data_source(self, item):
        pass

    @data_source.register
    def _(self, item: int):
        self.data = item

    @data_source.register
    def _(self, item: str):
        self.data = len(item)
        print(f'Initialized with string value, its length is: {self.data}')


obj3 = Sample(3000)
print(obj3)
obj4 = Sample('flflflfllf')
print(obj4)