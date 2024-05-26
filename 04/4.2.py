# 1
a, b = (int(input()) for _ in range(2))

print("Нельзя делить на 0" if b == 0 else a // b)


# 2
number = int(input())

if number % 100 == 39:
    print("YES")
else:
    print("NO")


# 3
print(f"Мангу{' можно ' if 2023 - int(input()) > 17 else ' нельзя '}купить")


# 4
print("YES" if len(input()) > 7 else "NO")


# 5
скорость_км_час, остаток_минут, расстояние_км = (
    float(input()),
    int(input()),
    float(input()),
)
минут_в_часе = 60
расстояние_минут = расстояние_км / скорость_км_час * минут_в_часе

if расстояние_минут <= остаток_минут:
    print("Сакура придет вовремя")
else:
    print(расстояние_минут - остаток_минут)


# 6
print("Сакура" if int(input()) % 2 == 0 else "Мику")
