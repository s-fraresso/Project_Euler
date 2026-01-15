divisor_count = [1]*(10**7)

for divisor in range(2, 10**7):
    multiple = divisor
    while multiple < 10**7:
        divisor_count[multiple] += 1
        multiple += divisor

print(sum(divisor_count[n] == divisor_count[n + 1] for n in range(2, 10**7 - 1)))