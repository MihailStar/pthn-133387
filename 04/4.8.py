# 1
print("YES" if 0 < int(input()) < 9 and 0 < int(input()) < 9 else "NO")


# 2
y1, x1, y2, x2 = (int(input()) for _ in range(4))

print("YES" if y1 == y2 or x1 == x2 else "NO")


# 3
y1, x1, y2, x2 = (int(input()) for _ in range(4))

print("YES" if (y1 + x1) % 2 == (y2 + x2) % 2 else "NO")


# 4
y1, x1, y2, x2 = (int(input()) for _ in range(4))

print("YES" if abs(y1 - y2) == abs(x1 - x2) else "NO")


# 5
y1, x1, y2, x2 = (int(input()) for _ in range(4))

if (y1 + x1) % 2 != (y2 + x2) % 2:
    print(-1)
elif y1 == y2 and x1 == x2:
    print(0)
elif abs(y1 - y2) == abs(x1 - x2):
    print(1)
else:
    print(2)


# 6
y1, x1, y2, x2 = (int(input()) for _ in range(4))

print("YES" if y1 == y2 or x1 == x2 or abs(y1 - y2) == abs(x1 - x2) else "NO")


# 7
y1, x1, y2, x2 = (int(input()) for _ in range(4))
can_walk = (
    (y1 - 1 == y2 and x1 == x2)
    or (y1 - 1 == y2 and x1 + 1 == x2)
    or (y1 == y2 and x1 + 1 == x2)
    or (y1 + 1 == y2 and x1 + 1 == x2)
    or (y1 + 1 == y2 and x1 == x2)
    or (y1 + 1 == y2 and x1 - 1 == x2)
    or (y1 == y2 and x1 - 1 == x2)
    or (y1 - 1 == y2 and x1 - 1 == x2)
)

print("YES" if can_walk else "NO")


# 8
y1, x1, y2, x2 = (int(input()) for _ in range(4))
can_eat = (
    abs(y1 - y2) == 2 and abs(x1 - x2) == 1 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1
)

print("YES" if can_eat else "NO")


# 9
y1, x1, y2, x2 = (int(input()) for _ in range(4))

if abs(y1 - y2) == 2 and abs(x1 - x2) == 1 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
    print("Конь бьет ладью")
elif y1 == y2 or x1 == x2:
    print("Ладья бьет коня")
else:
    print("Нет насилию")


# 10
y1, x1, y2, x2 = (int(input()) for _ in range(4))
figure = input()

if figure == "ладья" and (y1 == y2 or x1 == x2):
    print("Шах!")
elif figure == "слон" and (abs(y1 - y2) == abs(x1 - x2)):
    print("Шах!")
elif figure == "ферзь" and (y1 == y2 or x1 == x2 or abs(y1 - y2) == abs(x1 - x2)):
    print("Шах!")
elif figure == "конь" and (
    abs(y1 - y2) == 2 and abs(x1 - x2) == 1 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1
):
    print("Шах!")
