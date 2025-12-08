n = 0

for i in range(1, 501, 2):
    print(i)
    if i % 3 == 0:
        n += i

print(n)