import copy

# List containing other list elements
original_list = [["apple", "banana"], ["grapes", "orange"]]

#shallow copy
shallow_list = copy.copy(original_list)
shallow_list[0][0] = "pineapple"

#deep copy

original_list1 = [["apple", "banana"], ["grapes", "orange"]]
deep_list = copy.deepcopy(original_list1)

deep_list[0][0] = "peach"

print("Original:", original_list)
print("Shallow Copy:", shallow_list)
print("Deep Copy:", deep_list)