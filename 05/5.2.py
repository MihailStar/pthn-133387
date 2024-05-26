# 1
for n in range(1, int(input()) + 1):
    print(n)


# 2
for i in range(1, int(input()) + 1):
    n = int(input())

    if n % i == 0:
        print(n)


# 3
for n in range(1, int(input()) + 1):
    print(n**3)


# 4
from math import factorial

print(factorial(int(input())))


# 5
from functools import cache
from math import factorial


@cache
def fucktorial(n: int) -> int:
    return factorial(n)


for i in range(1, int(input()) + 1):
    print(fucktorial(i))


# 6
(b, n) = (input() for _ in range(2))

print(int(n, int(b)))
