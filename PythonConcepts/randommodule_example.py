import random

movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']
a = random.choice(movie_list)
print(a)

random.seed(5)
print(random.randint(1,100))