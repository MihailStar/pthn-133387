# 1
print(input().split()[2])


# 2
print(*input().split(), sep="\n")


# 3
print(sum(int(digit) for digit in input().split()))


# 4
numbers = [float(digit) for digit in input().split()]

print(sum(numbers) / len(numbers))
