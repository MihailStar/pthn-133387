# 1
strings = [input() for _ in range(3)]

print(sorted(strings)[0])


# 2
strings = [input() for _ in range(3)]

print(*sorted(strings), sep="\n")


# 3
numbers = [int(input()) for _ in range(3)]

print(sum(abs(number) for number in numbers))
print(abs(sum(numbers)))
