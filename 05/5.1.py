# 1
for i in range(10):
    print("Сакура, придумай какой-нибудь интересный текст и поставь сюда")


# 2
s = input()

for i in range(int(input())):
    print(s)


# 3
for _ in range(int(input())):
    print(f"Привет, {input()}")


# 4
acc = 0

for _ in range(int(input())):
    acc += int(input())

print(acc)


# 5
print(sum(num for num in (int(input()) for _ in range(int(input()))) if num > 0))


# 6
print(
    *(num for num in (int(input()) for _ in range(int(input()))) if num % 2 == 0),
    sep="\n",
)


# 7
print(min(int(input()) for _ in range(int(input()))), sep="\n")


# 8
print(
    *(num for num in (int(input()) for _ in range(int(input()))) if num < 4), sep="\n"
)


# 9
for grade in (int(input()) for _ in range(int(input()))):
    if grade < 0:
        print("Тоши взломал тестирующую систему")
    elif grade < 60:
        print("Сакура писала тест честно")
    elif 59 < grade < 80:
        print("Сакура списала с Мику")
    elif 79 < grade < 101:
        print("Сакура списала с Тоши")
    elif grade > 100:
        print("Сакура взломала тестирующую систему")


# 10
print(sorted([int(input()) for _ in range(int(input()))])[1])
