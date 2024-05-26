# 1
print(*reversed((input(), input(), input())), sep="\n")


# 2
print(
    *(
        string
        for index, string in enumerate(input() for _index in range(5))
        if index % 2 == 0
    ),
    sep="\n"
)


# 3
print(
    *(
        string
        for index, string in enumerate(input() for _index in range(5))
        if index % 2 == 0
    ),
    sep="\n"
)


# 4
a = "Этот текст изначально хранился в a"
b = "Этот текст изначально хранился в b"

a, b = b, a

print(a)
print(b)
