# 1
n, m = int(input()), int(input())
i = 1

for y in range(n):
    r: list[int] = []
    for x in range(m):
        r.append(i)
        i += 1
    print(*r)


# 2
n, m = int(input()), int(input())
i = 1

for y in range(n):
    r: list[int] = []
    for x in range(m):
        r.append(i)
        i += 1
    if y % 2 == 1:
        r.reverse()
    print(*r)


# 3
n, m = int(input()), int(input())
t: list[list[int]] = []

for y in range(1, n + 1):
    r: list[int] = []
    for x in range(1, m + 1):
        r.append(y * x)
    t.append(r)

print("\n".join(("\t".join(str(n) for n in r) for r in t)))


# 4
n = int(input())
t = ["" for _ in range(n)]

for y in range(n):
    t[-(y + 1)] = input()

print(*t, sep="\n")


# 5
n = int(input())
t = [[int(d) for d in input().split()] for _ in range(n)]

for x in range(n):
    r: list[int] = []
    for y in range(n):
        r.append(t[y][x])
    print(*r)
