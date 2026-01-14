from sympy import primerange

def count_sum(result, lowest_prime=2, memo={}):
    key = (result, lowest_prime)
    if key in memo:
        return memo[key]
    
    if result == 0:
        return 1
    
    nb_sums = 0
    for p in primerange(lowest_prime, result + 1):
        nb_sums += count_sum(result - p, p, memo)
    memo[key] = nb_sums
    return nb_sums


n = 2
while count_sum(n) <= 5_000:
    n += 1
print(n)