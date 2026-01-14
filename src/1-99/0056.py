def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


print(max(digit_sum(a**b) for a in range(1, 100) for b in range(100)))