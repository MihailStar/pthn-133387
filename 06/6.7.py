# 1
print("YES" if input().isalnum() else "NO")


# 2
for _ in range(int(input())):
    word = input()
    if word.islower():
        print(word)


# 3
word = input()

if word.isdigit():
    print("Это число")
elif word.isalpha():
    print("Это слово")
elif word.isalnum():
    print("Это буквы и цифры")
elif word.isspace():
    print("Это строка из пробельных символов")
else:
    print("Это что-то странное")


# 4
print(input().startswith(input()))
