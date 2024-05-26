# 1
def rectangle(a: int, b: int) -> None:
    print(("*" * b + "\n") * a)


rectangle(int(input()), int(input()))


# 2
def square(a: int, c: str) -> None:
    print((c * a + "\n") * a)


square(int(input()), input())


# 3
def line(n: int = 0) -> None:
    if n > 0:
        print("+" * n)
    elif n < 0:
        print("-" * abs(n))
    else:
        return


line(int(input()))


# 4
def triangle(n: int) -> None:
    for i in range(1, n + 1):
        print("*" * i)


triangle(int(input()))


# 5
def frame(a: int, b: int) -> None:
    print(f'+{"-"*(b - 2)}+')
    for _ in range(a - 2):
        print(f'|{" "*(b - 2)}|')
    print(f'+{"-"*(b - 2)}+')


frame(int(input()), int(input()))


# 6
def rectangle(y: int, x: int) -> None:
    print(("*" * x + "\n") * y)


n, m = int(input()), int(input())

rectangle(n, m)

rectangle(3, 4)

rectangle(m, n)

rectangle(5, 5)

rectangle(m, n)
