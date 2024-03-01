class SingletonPattern:
    _instance = None

    def __init__(self):
        raise Exception("its a singleton pattern implementation")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


a = SingletonPattern.get_instance()

b = SingletonPattern.get_instance()

print(a is b)
