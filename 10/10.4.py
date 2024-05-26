# 1
from random import randrange, seed

coin = {"решка": 0, "орел": 1}

for internal_state in range(1_000_000 + 1):
    seed(internal_state)

    for i in range(20):
        if randrange(len(coin)) == coin["орел"]:
            break
    else:
        print(internal_state)
        break
else:
    print(None)
