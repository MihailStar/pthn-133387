# 1
n, m = int(input()), int(input())

print([[0 for _ in range(m)] for _ in range(n)])


# 2
print([[int(d) for d in input().split()] for _ in range(int(input().split()[0]))])


# 3
print([n for n in (int(d) for d in input().split()) if n % 2 == 0])
