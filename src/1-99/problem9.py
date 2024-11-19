def special_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - b - a
            if a**2 + b**2 == c**2:
                return a*b*c
    return 0


print(special_triplet())