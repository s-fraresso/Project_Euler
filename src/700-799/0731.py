def A(n):
    digits = ""
    for i in range(10):
        digits += str(((10 * pow(10, n + i - 1, 2999)) // 2999) % 10)
    return int(digits)


print(A(10**16))