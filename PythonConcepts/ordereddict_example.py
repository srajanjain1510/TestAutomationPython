from collections import OrderedDict

numbers_ord_dict = OrderedDict(one='srajan', two='ankita', three='satvik', four='punyavi')

print(numbers_ord_dict)

for values in numbers_ord_dict.values():
    print(values)

for key, values in numbers_ord_dict.items():
    print(key, values)

# unique feature of ordered dict ---.move_to_end() method

numbers_ord_dict.move_to_end('four', False)

print(numbers_ord_dict)

numbers_ord_dict.move_to_end('four', True)

print(numbers_ord_dict)

# unique feature of ordered dict ---popitem method

numbers_ord_dict.popitem(last=True)

print(numbers_ord_dict)

numbers_ord_dict['four'] = 'punyavi'

print(numbers_ord_dict)

numbers_ord_dict.popitem(last=False)

print(numbers_ord_dict)