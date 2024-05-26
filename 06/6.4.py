# 1
print(input().lower())


# 2
print("YES" if input().lower() == input().lower() else "NO")


# 3
password = input()

print(
    "YES"
    if len(password) > 7
    and password != password.lower()
    and password != password.upper()
    else "NO"
)
