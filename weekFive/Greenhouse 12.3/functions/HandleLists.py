import random

my_dict = {}

def makeList(key, value):
    if key in my_dict:
        my_dict[key].append(value)
    else:
        my_dict[key] = [value]

    return my_dict.get(key, [])

makeList("one", random.randint(1, 10))
makeList("one", random.randint(1, 10))
one = makeList("one", random.randint(1, 10))
makeList("two", random.randint(11, 20))
makeList("two", random.randint(11, 20))
two = makeList("two", random.randint(11, 20))
makeList("three", random.randint(21, 31))
makeList("three", random.randint(21, 31))
three = makeList("three", random.randint(21, 31))

print(one)
print(two)
print(three)