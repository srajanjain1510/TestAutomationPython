
language = ['java','python']
version = [21,3.11]

result = list(zip(language,version))

print(result)

#unzip

language,version = zip(*result)

print(language)
print(version)

