"""
OEIS A000931 padovan sequence = count_palindromic_sums_without_2
"""

def count_palindromic_sums_without_2(n, memo={0:1, 1:1, 2:1}):
    if n in memo:
        return memo[n]
    
    nb_sums = 1 # (n)

    for k in range(1, n // 2 + 1):
        if k != 2:
            nb_sums += count_palindromic_sums_without_2(n - 2 * k, memo)
    
    memo[n] = nb_sums
    return nb_sums


def t(n):
    return 2**(n // 2) - count_palindromic_sums_without_2(n)

n = 4

nb_palindromic_sums = 2**(n // 2) % 1_000_000

p_2 = count_palindromic_sums_without_2(n - 2) % 1_000_000
p_1 = count_palindromic_sums_without_2(n - 1) % 1_000_000
p_curr = count_palindromic_sums_without_2(n) % 1_000_000

while (nb_palindromic_sums - p_curr) % 1_000_000 != 0:
    n += 1

    if n % 2 == 0:
        nb_palindromic_sums = (nb_palindromic_sums * 2) % 1_000_000

    temp = p_curr
    p_curr = (p_1 + p_2) % 1_000_000
    p_2 = p_1
    p_1 = temp
    

print(n)