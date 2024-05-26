# 1
s = input()

print(f"{s[:5]}..." if len(s) > 5 else s)


# 2
s = input()

print(f"{s[:5]}..." if len(s) > 5 else s)


# 3
s = input()
n = len(s) // 3

print(s[:n])
print(s[n : n * 2])
print(s[n * 2 : n * 3])


# 4
s = input()

print("YES" if s == s[::-1] else "NO")
