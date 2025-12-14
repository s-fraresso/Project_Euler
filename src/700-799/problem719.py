from itertools import combinations


def is_s_number(n):
    root = int(n**(1/2))
    digit_list = list(str(n))
    nb_digits = len(digit_list)

    for nb_split in range(nb_digits - 1, 0, -1):
        max_possible_sum = 10**(nb_digits - nb_split) - 1 + 9 * nb_split
        if max_possible_sum < root:
            continue

        for split in combinations(range(1, nb_digits), nb_split):
            indexes = (0,) + split + (nb_digits,)
            if sum(int(''.join(digit_list[indexes[i]:indexes[i + 1]])) for i in range(len(indexes) - 1)) == root:
                return True
        
    return False


def T(N):
    res = 0
    for i in range(1, int(N**(1/2) + 1)): 
        n = i**2
        if is_s_number(n):
            res += n
    return res


print(T(10**4))
print(T(10**12))
