# 1
print(input().replace("Ё", "Е").replace("ё", "е"))


# 2
print(input().replace("А", "").replace("а", ""))


# 3
s = input()
s_copy = ""

for char in s:
    if char in ("а", "е", "и", "о", "у", "ы", "э", "ю", "я", "ё"):
        s_copy += "у"
    else:
        s_copy += char

print(s_copy)


# 4
print(input().replace(" ", "\n"))
