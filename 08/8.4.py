# 1
n = int(input())

for y in range(n):
    r: list[int] = []
    for x in range(n):
        r.append(1 if y == x else 0)
    print(*r)


# 2
n = int(input())

for y in range(n):
    r: list[int] = []
    for x in range(n):
        if y > x:
            r.append(2)
        elif y < x:
            r.append(0)
        else:
            r.append(1)
    print(*r)


# 3
n = int(input())

for y in range(n):
    r: list[int] = []
    for x in range(n):
        if y + x == n - 1:
            r.append(1)
        else:
            r.append(0)
    print(*r)


# 4
n = int(input())

for y in range(n):
    r: list[int] = []
    for x in range(n):
        if y + x > n - 1:
            r.append(2)
        elif y + x < n - 1:
            r.append(0)
        else:
            r.append(1)
    print(*r)


# 5
n = int(input())

# @tutorial https://stepik.org/lesson/886428/step/7?discussion=7483564&unit=891118

for y in range(n):
    r: list[int] = []
    for x in range(n):
        if y == x or y + x == n - 1:
            r.append(1)
        elif y < x and y < n - 1 - x:
            r.append(2)
        elif y < x and y > n - 1 - x:
            r.append(3)
        elif y > x and y > n - 1 - x:
            r.append(4)
        elif y > x and y < n - 1 - x:
            r.append(5)
    print(*r)


# 6
n = int(input())

# @tutorial https://stepik.org/lesson/886428/step/8?discussion=7638682&unit=891118

for y in range(n):
    r: list[int] = []
    for x in range(n):
        r.append(abs(y - x))
    print(*r)


# 7
n = int(input())

# @tutorial https://stepik.org/lesson/886428/step/9?discussion=7675857&unit=891118

for y in range(n):
    r: list[int] = []
    for x in range(n):
        r.append(abs(y + x - n + 1))
    print(*r)


# 8
n, k = int(input()), int(input())
sequence = [*range(k)]

for y in range(n):
    r: list[int] = []
    for x in range(n):
        r.append(sequence[(y + x) % len(sequence)])
    print(*r)
