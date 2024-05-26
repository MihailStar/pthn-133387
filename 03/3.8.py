# 1
print(int(input()) + int(input()))


# 2
print(int(input()) * int(input()) + int(input()) * int(input()))


# 3
print(sum(n for n in range(1, int(input()) + 1)))


# 4
h, m, t = (int(input()) for _ in range(3))
end = h * 60 + m + t

print(((end // 60) % 24), (end % 60), sep="\n")


# 5
n, m = (int(input()) for _ in range(2))

print(n // m + 1 if n % m > 0 else n // m + 0)
