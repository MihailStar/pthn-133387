# 1
l = [[10, 12, 13], [17, 39, 81], [14, 66, 39]]

for sub_l in l:
    print(*sub_l)


# 2
y, x = map(int, input().split())

for _ in range(y):
    print(*["0"] * x)


# 3
n = int(input())

for _ in range(n):
    print(*["1"] * (n // 2) + ["0"] * (n // 2))


# 4
n, m = map(int, (input(), input()))
matrix: list[list[int]] = []

for _ in range(n):
    row: list[int] = []

    for x in range(1, m + 1):
        row.append(x)

    matrix.append(row)

for y in range(n):
    print(*matrix[y])


# 5
from itertools import cycle, islice

n = int(input())
matrix: list[list[int]] = []

for y in range(n):
    row: list[int] = []
    sequence = (0, 1) if y % 2 == 0 else (1, 0)

    for x in islice(cycle(sequence), n):
        row.append(x)

    matrix.append(row)

for y in range(n):
    print(*matrix[y])


# 6
n, _m = map(int, (input(), input()))
matrix: list[list[int]] = []

for _ in range(n):
    matrix.append([int(d) for d in input().split()])

print(matrix)
