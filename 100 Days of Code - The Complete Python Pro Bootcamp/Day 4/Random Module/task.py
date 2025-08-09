import random
# random_int = random.randint(1, 10)
# print(random_int)

# random_float = random.random()
# print(random_float)

# random_uniform = random.uniform(1, 10)
# print(random_uniform)

coin = random.uniform(0, 1)
if coin <= 0.5:
    print("Heads")
else :
    print("Tails")