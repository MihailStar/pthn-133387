# 1
s = "Строка"

print(s[0])


# 2
print(*(char for index, char in enumerate(input()) if index % 2 == 0), sep="")


# 3
print(input()[-1])


# 4
string = input()

if len(string) % 2 == 0:
    print("Нет центрального символа")
else:
    print(string[len(string) // 2])


# 5
print(input()[-1])
