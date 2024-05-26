# 1
from random import randrange

for _ in range(int(input())):
    print(randrange(1, 39 + 1))


# 2
from random import randrange

for _ in range(int(input())):
    print(randrange(0, 100, 2))


# 3
from random import randint

for _ in range(int(input())):
    print(randint(1, 6))


# 4
from random import randint

for _ in range(int(input())):
    random = randint(1, 1000)

    if random < 500:
        print("орел")
    elif random > 500:
        print("решка")
    else:
        print("ребро")


# 5
from random import randint

bet = input()
slot_number = randint(0, 36)
slot_color = "зеленый"
is_odd = slot_number % 2 == 0

if 0 < slot_number < 11 or 18 < slot_number < 29:
    slot_color = "черный" if is_odd else "красный"
elif 10 < slot_number < 19 or 28 < slot_number < 37:
    slot_color = "красный" if is_odd else "черный"

print(f"ставка{' ' if bet == slot_color else ' не '}сыграла")
