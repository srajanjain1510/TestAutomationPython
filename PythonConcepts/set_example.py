s1 = {1, 2}

s2 = {'a': 'e', 'e': 'f'}

s1.update(s2)
s1.add('epam')
print(s1)

list_num = [1, 2, 4, 5, 6, 7, 7]


def modify_list(some_list, item):
    some_list.append(item)


list_num = [1, 2, 4, 5, 6, 7, 7]
modify_list(list_num, 434343)
print(list_num)


def outer_function(text):
    name = text

    def inner_function():
        print(f"Hi {name}")

    return inner_function

my_func = outer_function('dkdkd')
my_func()