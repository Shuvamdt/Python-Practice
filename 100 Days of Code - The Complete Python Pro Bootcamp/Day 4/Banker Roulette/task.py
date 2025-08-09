import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

num = random.randint(0, len(friends)-1)
billPayer = friends[num]
print(f"{billPayer} will pay the bill!")

print(random.choices(friends))