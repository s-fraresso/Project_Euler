def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


powerful_numbers = set()

for base in range(2, 100):
    power = 2
    for power in range(2, 10):
        if digit_sum(base**power) == base:
            powerful_numbers.add((base**power))
        power += 1

print(sorted(powerful_numbers)[29])