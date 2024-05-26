# 1
a, b, c = (int(input()) for _ in range(3))

print("YES" if a + b >= c and c + a >= b and b + c >= a else "NO")


# 2
n = int(input())

if n % 2 == 0:
    print("число n четно")
else:
    print("число n нечетно")

if n % 5 == 0 and n % 2 == 0:
    print("число n делится на 10")
else:
    print("число n не делится на 10")
