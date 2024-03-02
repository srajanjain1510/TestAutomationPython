import random


def generate_incremental_random_number():
    number = random.randint(10000, 9999999)
    yield number


print(next(generate_incremental_random_number()))


