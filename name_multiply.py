name = 'Nate O'
name_by_100 = name * 100
print(name_by_100)


def banner(message):
    stars = '*' * len(message)
    print(stars)
    print(message)
    print(stars)


print(name[0])

for letter in name:
    print(letter)

for index, letter in enumerate(name):
    print(letter * (index +1))