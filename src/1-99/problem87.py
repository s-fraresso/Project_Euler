from sympy import primerange

def build_prime_power_sum(powers, upper_bound, current_sum=0):
    if len(powers) == 0:
        return {current_sum}
    
    sums = set()
    for p in primerange(upper_bound):
        new_sum = current_sum + p**powers[0]
        if new_sum >= upper_bound:
            break
        sums.update(build_prime_power_sum(powers[1:], upper_bound, new_sum))

    return sums

print(len(build_prime_power_sum((2, 3, 4), 50_000_000)))
