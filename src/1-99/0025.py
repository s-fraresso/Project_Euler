def first_n_digit_fibonacci(n):
    k = 1
    current, next = 1, 1
    while len(str(current)) < n:
        temp = next
        next = current + next
        current = temp
        k += 1
    return k

print(first_n_digit_fibonacci(1_000)) # 4782