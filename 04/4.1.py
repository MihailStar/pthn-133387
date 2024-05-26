# 1
print("четное" if int(input()) % 2 == 0 else "нечетное")


# 2
a, b, x = (int(input()) for _ in range(3))

print("YES" if a <= x <= b else "NO")


# 3
n = int(input())

print("YES" if 1 <= n <= 4 else "NO")


# 4
from random import choice

a, b = (int(input()) for _ in range(2))

if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(choice((a, b)))


# 5
print("YES" if len(input()) == 5 else "NO")


# 6
rest = int(input()) % int(input())

print("Лишних конфет не осталось :(" if rest == 0 else rest)
