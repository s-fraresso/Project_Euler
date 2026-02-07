UPPER_BOUND = 10**14
stealthy_numbers = set()

for x in range(1, int(UPPER_BOUND**(1/2))):
    for y in range(1, x + 1):
        if x * (x + 1) * y * (y + 1) >= UPPER_BOUND:
            break
        stealthy_numbers.add(x * (x + 1) * y * (y + 1))

print(len(stealthy_numbers))