# 1
for n in range(int(input()), int(input())):
    print(n)


# 2
for n in range(int(input()), int(input()), int(input())):
    print(n)


# 3
a, b = (int(input()) for _ in range(2))

for n in range(a if a % 2 == 0 else a + 1, b, 2):
    print(n)


# 4
a, b = (int(input()) for _ in range(2))

for n in range(a, b, -1 if a > b else 1):
    print(n)


# 5
from math import comb

n, m = (int(input()) for _ in range(2))

print(comb(n, m))
