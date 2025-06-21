def last_n_digit(k, n):
    return str(k)[-n:]

def sum_self_powers(n):
    total = 0
    for k in range(1, n + 1):
        total += k**k
    return total

print(last_n_digit(sum_self_powers(1_000), 10)) # 9110846700

