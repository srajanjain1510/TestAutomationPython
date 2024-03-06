from builder_pattern import Director, ConcreteBuilder


myBuilder = ConcreteBuilder()
director = Director(myBuilder)
house = director.construct_house()
house.list_parts()




