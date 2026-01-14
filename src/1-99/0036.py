def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False
    return True

def sum_doublebase_palindrome(limit):
    total = 0
    for n in range(1, limit):
        if is_palindrome(str(n)) and is_palindrome(str(bin(n))[2:]):
            total += n
    return total

print(sum_doublebase_palindrome(1_000_000)) # 872187