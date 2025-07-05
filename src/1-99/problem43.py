total = 0

for a in range(17, 1000, 17):
    for b in range(14, 1000, 7):
        if ((b % 10) * 100 + a // 10) % 13 != 0 or ((b % 100) * 10 + a // 100) % 11 != 0:
            continue
        for c in range(12, 1000, 2):
            if ((c % 10) * 100 + b // 10) % 5 != 0 or ((c % 100) * 10 + b // 100) % 3 != 0:
                continue
            for d in range(10):
                number = ''.join((str(d), str(c).zfill(3), str(b).zfill(3), str(a).zfill(3)))
                if sorted(list(number)) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    total += int(number)

print(total)