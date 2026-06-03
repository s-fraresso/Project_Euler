from numba import njit


@njit
def T(n):
    sum_2025_numbers = 0

    for root in range(4, int(10**(n / 2))):
        square = root**2
        nb_digits = len(str(square))

        a = square // 10**(nb_digits // 2)
        b = square % 10**(nb_digits // 2)

        if b // 10**(nb_digits // 2 - 1) != 0 and (a + b)**2 == square:
            sum_2025_numbers += square

    return sum_2025_numbers

T(0)
print(T(16))