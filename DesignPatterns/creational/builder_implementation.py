from builder_pattern import Director, ConcreteBuilder

director = Director()
myBuilder = ConcreteBuilder()
director.set_builder(myBuilder)
myBuilder.set_door_type("single")
myBuilder.set_roof_type("plain")
myBuilder.set_num_stories(4)
print(director.construct())




