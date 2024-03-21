vowels = ('a', 'e', 'i', 'o', 'u')

fset = frozenset(vowels)

print(fset)

dict = {'a': 56, 's': 54}

fset_dict = frozenset(dict)

print(fset_dict)

s = {'a', 'b'}

t = {'b', 'c'}

u = {'c', 'd','a'}

union_set = s.difference(t, u)

print(union_set)

#set comprehension

