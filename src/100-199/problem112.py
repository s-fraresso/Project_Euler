def is_increasing(n):
    return n < 10 or (n % 10 >= n // 10 % 10 and is_increasing(n // 10))

def is_decreasing(n):
    return n < 10 or (n % 10 <= n // 10 % 10 and is_decreasing(n // 10))

def is_bouncy(n):
    return not (is_increasing(n) or is_decreasing(n))

def find_bouncy_proportion(proportion):
    nb_bouncy = 0
    n = 1
    while nb_bouncy * 100 < proportion * n:
        n += 1
        if is_bouncy(n):
            nb_bouncy += 1
    return n

print(find_bouncy_proportion(99)) # 1587000