# 1
from random import choice


def vibrat_sluchainii_element(l: list):
    return choice(l)


l = [1, 2, 3, 4, 5, 39, 12345]

for i in range(1000):
    print(vibrat_sluchainii_element(l))


# 2
from random import choice

print(
    choice(
        ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    ),
    choice(["червей", "бубно", "треф", "пик"]),
)
