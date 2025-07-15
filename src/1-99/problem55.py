def reverse_number(n):
    reversed_n = 0
    while n > 0:
        reversed_n = 10 * reversed_n + (n % 10)
        n //= 10
    return reversed_n


def is_lychrel_number(n):
    rev = reverse_number(n)
    for _ in range(50):
        n = rev + n
        rev = reverse_number(n)
        if n == rev:
            return False
    return True


print(sum(is_lychrel_number(n) for n in range(1, 10_000)))