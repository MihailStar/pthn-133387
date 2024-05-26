# 1
def add_one(n: int) -> int:
    return n + 1


print(add_one(int(input())))


# 2
def s(a: int, b: int) -> int:
    return a + b


print(s(int(input()), int(input())))


# 3
def f(a: int, b: int) -> str:
    if a < 0:
        if b < 0:
            return "Оба числа отрицательны"
        return "Есть отрицательное число"
    if a == 0 or b == 0:
        return "Есть 0"
    return "Оба числа положительны"


print(f(int(input()), int(input())))


# 4
def v(a: int, b: int, c: int) -> int:
    return a * b * c


print(v(*[int(i) for i in input().split()]))


# 5
def s(a: int, b: int, c: int) -> int:
    return (a * b + b * c + c * a) * 2


print(s(*(int(i) for i in input().split())))


# 6
def edges_sum(a: int, b: int, c: int) -> int:
    return (a + b + c) * 4


print(edges_sum(*(int(i) for i in input().split())))
