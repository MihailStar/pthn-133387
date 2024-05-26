# 1
print(input().swapcase())


# 2
print(*(name.title() for name in input().split()))


# 3
s = input()

print("YES" if s != s.swapcase() else "NO")


# 4
s = input()

print(s[: len(s) // 2].capitalize(), s[len(s) // 2 :].capitalize(), sep="")
