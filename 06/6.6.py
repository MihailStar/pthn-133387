# 1
message = input()
index = message.find("Сакура")

if index == -1:
    print("Это письмо не Сакуре")
else:
    print(index)


# 2
print(input().count(" ") + 1)


# 3
print(input().count("@"))


# 4
# print([char != char.lower() for char in list(input())].count(True))

print(len([char for char in list(input()) if char != char.lower()]))


# 5
n, k, s = int(input()), int(input()), input()
string = s.lower()
words = [input() for _ in range(n)]

print(k * sum(string.count(word) for word in words))
