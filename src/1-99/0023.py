from sympy import divisors


def non_abundant_sum(threshold):
    total = 0
    abundant_sum = set()
    abundants = []
    for i in range(1, threshold):
        proper_divisor_sum = sum(divisors(i)) - i
        if proper_divisor_sum > i:
            abundants.append(i)
            for b in abundants:
                abundant_sum.add(i + b)
        if i not in abundant_sum:
            total += i
    return total


print(non_abundant_sum(28_123))