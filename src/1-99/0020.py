from math import factorial

def factorial_digit_sum(n):
    string = str(factorial(n))
    total = 0
    for c in string:
        total += int(c)
    return total

print(factorial_digit_sum(10))
print(factorial_digit_sum(100))