def outer_function(text):
    def inner_function():
        print('Hi',text)

    return inner_function

output = outer_function('Jodf')
print(output())
if hasattr(outer_function('Jod'),'__closure__'):
    print("uerrrr")


