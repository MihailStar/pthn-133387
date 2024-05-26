# 1
number = int(input())

if number > 0:
    print("+")
elif number < 0:
    print("-")
else:
    print("Число равно 0")


# 2
def is_leap(year: int) -> bool:
    """@tutorial https://github.com/mihailstar/pthn-cd/blob/master/10.2/index.py#L32"""

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print("YES" if is_leap(int(input())) else "NO")


# 3
print(max(int(input()) for _ in range(4)))


# 4
digit = input()

print(
    "YES"
    if not digit.startswith("-") and "3" in digit and "9" in digit and len(digit) < 5
    else "NO"
)


# 5
n = int(input())
is_not_odd = n % 2 == 1

if 0 < n < 11 or 18 < n < 29:
    print("красный" if is_not_odd else "черный")
elif 10 < n < 19 or 28 < n < 37:
    print("черный" if is_not_odd else "красный")
else:
    print("зеленый")


# 6
n = int(input())

if n in (1, 2, 4):
    print(n)
elif n == 3:
    print(6)
else:
    print(0)
