total = 0
for n in range(1, 10):
    i = 1
    while len(str(n**i)) == i:
        total += 1
        i += 1
print(total)