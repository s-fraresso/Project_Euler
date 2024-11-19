def is_palindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def largest_palindrome_product(n):
    largest = 1
    for i in range(1, int(10**n)):
        for j in range(i, int(10**n)):
            product = i * j
            if product > largest and is_palindrome(product):
                largest = product
    return largest


print(largest_palindrome_product(3))