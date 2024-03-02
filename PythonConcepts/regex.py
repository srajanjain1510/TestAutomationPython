import re

s = '123arwrewrwrwrwbc4512ab'

re_search = re.search('ab', s)

print(re_search)

re_search_1 = re.search('123[ade]', s)
print(re_search_1)

re_search_2 = re.search('[0-9$]', s)
print(re_search_2)

s = r'foo\bar'
re_search_3 = re.search('\\\\', s)
print(re_search_3)
