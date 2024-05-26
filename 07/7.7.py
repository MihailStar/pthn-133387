# 1
l = [1, 2, 3, 4, 5, 6, 39, 0, 1, -100]

l.reverse()

print(l)


# 2
l = [5, 4, 5, 3, 4, 5, 4, 4, 3, 5, 4, 5, 5]

# for _ in filter(lambda grade: grade == 5, l):
#     print("Сакура молодец!")

print("Сакура молодец!\n" * l.count(5))
