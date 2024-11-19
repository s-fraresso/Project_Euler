from fractions import Fraction

def sum_digit_convergent(n):
    total = 0
    string = str((convergent_of_e(n)).numerator)
    print(convergent_of_e(n))
    for c in string:
        total += int(c)
    return total


def convergent_of_e(n):
    if n == 1:
        return Fraction(2)
    u_i = Fraction(2 * (n // 3) if n % 3 == 0 else 1)
    for i in range(n - 1, 0, -1):
        if i == 1:
            u_i = 2 + 1 / u_i
        else:
            u_i = (2 * (i // 3) if i % 3 == 0 else 1) + 1 / u_i
    return u_i

        
print(sum_digit_convergent(100))
