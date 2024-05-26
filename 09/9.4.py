# 1
def s(r: float) -> float:
    pi = 3.1415
    return pi * r**2


print(s(float(input())))


# 2
def cylinder_volume(r: float, h: float) -> float:
    pi = 3.1415
    return pi * r**2 * h


r, h = (float(i) for i in input().split())

print(cylinder_volume(r, h))


# 3
def cylinder_surface_area(r: float, h: float) -> float:
    pi = 3.1415
    return 2 * pi * r**2 + 2 * pi * r * h


r, h = (float(i) for i in input().split())

print(cylinder_surface_area(r, h))


# 4
def sphere_volume(r: float) -> float:
    pi = 3.1415
    return 4 / 3 * pi * r**3


print(sphere_volume(float(input())))


# 5
def avg(a: int, b: int, c: int) -> int:
    return sorted((a, b, c))[1]


print(avg(int(input()), int(input()), int(input())))


# 6
from math import sqrt


def s(a: float, b: float, c: float) -> float:
    if a + b < c or b + c < a or c + a < b:
        return -1

    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))

    return round(s, 3)


print(s(float(input()), float(input()), float(input())))
