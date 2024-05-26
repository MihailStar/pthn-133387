# 1
print(sum(int(digit) for digit in iter(input, "0")))


# 2
max_volume = int(input())
volume = 0
counter = 0

while volume < max_volume:
    new_volume = volume + int(input())

    if new_volume > max_volume:
        break

    volume = new_volume
    counter += 1

print(counter)


# 3
print(sum(1 for _ in iter(input, "Пентагон взломан")) + 1)


# 4
n = int(input())
c = 0

while n > 1:
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1

    c += 1

print(c)
