import random

names = []

while len(names) < 8:
    names_add = input("Type one name: ")
    names.append(names_add)

print(names[random.randint(0,7)])

