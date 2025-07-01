from math import sqrt


def generate_split_sums(n, nb_split, memo=dict()):
    if (tuple(n), nb_split) in memo:
        return memo[(tuple(n), nb_split)]
    if nb_split == 0:
        return [int(''.join(n))]
    sums = []
    for end_idx in range(len(n) - nb_split):
        current_term = int(''.join(n[:end_idx + 1]))
        for subsum in generate_split_sums(n[end_idx + 1:], nb_split - 1):
            sums.append(current_term + subsum)
    memo[(tuple(n), nb_split)] = sums
    return sums

def test_s_number(i, n):
    for nb_split in range(1, len(n)):
        for split_sum in generate_split_sums(n, nb_split):
            if split_sum == i:
                return True
    return False

def T(N):
    res = 0
    for i in range(1, int(sqrt(N) + 1)):
        if i % 1000 == 0:
            print(i)    
        n = list(str(i**2))
        if test_s_number(i, n):
            res += i**2
    return res


# print(test_s_number(9, ['8','1']))
# print(test_s_number(82, ['6','7','2','4']))
# print(test_s_number(91, ['8','2','8','1']))
# print(test_s_number(99, ['9','8','0','1']))

print(T(10**12))
