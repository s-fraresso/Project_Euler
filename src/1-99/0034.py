factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def is_digit_factorials(n):
    tmp_n = n
    fact_sum = 0
    while n != 0:
        fact_sum += factorial[n % 10]
        n //= 10
    return fact_sum == tmp_n
    

def sum_digit_factorials():
    total = 0
    for k in range(3, 10**7):
        if is_digit_factorials(k):
            total += k
    return total


print(sum_digit_factorials()) # 40730