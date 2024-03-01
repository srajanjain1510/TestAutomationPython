def singleton_decorator(class_):
    instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return wrapper


@singleton_decorator
class MyClass:
    def __init__(self, x):
        self.x = x


a = MyClass('a')
b = MyClass('b')

if (a is b):
    print('instances are same')
