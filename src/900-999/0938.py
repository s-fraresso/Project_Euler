from sys import setrecursionlimit
setrecursionlimit(1000000)

def P(R, B, memo = {}):
    if (R, B) in memo:
        return memo[(R, B)]

    if R == 0:
        return 1
    if B == 0:
        return 0

    N = (B + R) * (B + R - 1) / 2

    red_black = (R * B / N) * P(R, B - 1)
    red_red = (R * (R - 1) / 2) / N * P(R - 2, B) if R > 1 else 0

    total = red_black + red_red

    if B > 1:
        total *= 2 * N / (2 * N - B * (B - 1))
    
    memo[(R, B)] = total
    return total


print(P(24690, 12345))


    